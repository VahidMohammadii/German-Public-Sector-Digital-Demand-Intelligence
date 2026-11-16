#!/usr/bin/env python3
"""Load a DÖE CSV export into source-isolated MySQL staging tables.

The script intentionally keeps source rows at their published grain. It does
not classify threshold status, select a latest notice version, or merge DÖE
identifiers with TED identifiers.
"""

from __future__ import annotations

import argparse
import csv
import getpass
import re
import sys
import zipfile
from collections import Counter
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, TextIO


REQUIRED_NOTICE_COLUMNS = {
    "noticeIdentifier",
    "noticeVersion",
    "procedureLegalBasis",
    "publicationDate",
}
SAFE_NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
KEY_TYPES = {
    "noticeIdentifier": "VARCHAR(128)",
    "noticeVersion": "VARCHAR(32)",
    "lotIdentifier": "VARCHAR(128)",
}
RESERVED_COLUMNS = {"row_id", "export_month", "loaded_at_utc"}


def table_name(csv_name: str) -> str:
    stem = Path(csv_name).stem
    snake = re.sub(r"(?<!^)(?=[A-Z])", "_", stem).lower()
    result = f"doe_raw_{snake}"
    if not SAFE_NAME.fullmatch(result):
        raise ValueError(f"Unsupported CSV filename: {csv_name}")
    return result


@contextmanager
def open_csv_sources(source: Path) -> Iterator[list[tuple[str, TextIO]]]:
    """Open all CSV files in a folder or ZIP while keeping filenames stable."""
    if source.is_dir():
        files = sorted(p for p in source.rglob("*.csv") if p.is_file())
        if not files:
            raise ValueError("The selected folder contains no CSV files.")
        opened: list[tuple[str, TextIO]] = []
        try:
            for path in files:
                opened.append((path.name, path.open("r", encoding="utf-8-sig", newline="")))
            yield opened
        finally:
            for _, handle in opened:
                handle.close()
        return

    if not source.is_file() or not zipfile.is_zipfile(source):
        raise ValueError("Select a DÖE CSV ZIP file or a folder containing extracted CSV files.")

    with zipfile.ZipFile(source) as archive:
        members = sorted(
            name for name in archive.namelist()
            if name.lower().endswith(".csv") and not name.endswith("/")
        )
        if not members:
            raise ValueError("The selected ZIP contains no CSV files.")
        names = [Path(name).name for name in members]
        if len(names) != len(set(names)):
            raise ValueError("The ZIP contains duplicate CSV filenames in different folders.")
        opened = []
        try:
            for member in members:
                import io
                opened.append((Path(member).name, io.TextIOWrapper(archive.open(member), encoding="utf-8-sig", newline="")))
            yield opened
        finally:
            for _, handle in opened:
                handle.close()


def inspect_sources(sources: list[tuple[str, TextIO]]) -> list[dict]:
    specs = []
    seen_tables = set()
    for filename, handle in sources:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames
        if not headers or any(not h for h in headers) or len(headers) != len(set(headers)):
            raise ValueError(f"{filename} must have a non-empty header row with unique column names.")
        reserved = RESERVED_COLUMNS.intersection(headers)
        if reserved:
            raise ValueError(f"{filename} uses reserved staging columns: {', '.join(sorted(reserved))}")
        name = table_name(filename)
        if name in seen_tables:
            raise ValueError(f"More than one CSV maps to staging table {name}.")
        seen_tables.add(name)

        row_count = 0
        notice_keys = set()
        notice_ids = set()
        legal_basis = Counter()
        for row in reader:
            if None in row:
                raise ValueError(f"{filename} contains a row with more values than its header.")
            row_count += 1
            if filename.lower() == "notice.csv":
                notice_ids.add(row.get("noticeIdentifier", ""))
                notice_keys.add((row.get("noticeIdentifier", ""), row.get("noticeVersion", "")))
                legal_basis[row.get("procedureLegalBasis") or "[blank]"] += 1
        if filename.lower() == "notice.csv" and not REQUIRED_NOTICE_COLUMNS.issubset(headers):
            missing = sorted(REQUIRED_NOTICE_COLUMNS.difference(headers))
            raise ValueError(f"notice.csv is missing required columns: {', '.join(missing)}")
        handle.seek(0)
        specs.append({
            "filename": filename,
            "table": name,
            "headers": headers,
            "row_count": row_count,
            "notice_ids": notice_ids if filename.lower() == "notice.csv" else None,
            "notice_keys": notice_keys if filename.lower() == "notice.csv" else None,
            "legal_basis": legal_basis if filename.lower() == "notice.csv" else None,
        })
    return specs


def print_summary(specs: list[dict], export_month: str) -> None:
    print(f"DÖE export month: {export_month}")
    print(f"CSV tables: {len(specs)}")
    print(f"Total CSV rows: {sum(item['row_count'] for item in specs):,}")
    notice = next((item for item in specs if item["filename"].lower() == "notice.csv"), None)
    if notice:
        print(f"Notice versions: {len(notice['notice_keys']):,}")
        print(f"Distinct notice identifiers: {len(notice['notice_ids']):,}")
        blank = notice["legal_basis"].get("[blank]", 0)
        print(f"Notice versions without procedureLegalBasis: {blank:,}")
    print("Staging tables:")
    for item in specs:
        print(f"  {item['table']}: {item['row_count']:,} rows")


def quote_identifier(identifier: str) -> str:
    if not SAFE_NAME.fullmatch(identifier):
        raise ValueError(f"Unsafe SQL identifier: {identifier}")
    return f"`{identifier}`"


def column_type(header: str) -> str:
    return KEY_TYPES.get(header, "LONGTEXT")


def ensure_table(cursor, database: str, table: str, headers: list[str]) -> None:
    qtable = quote_identifier(table)
    definitions = [
        "`row_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT",
        "`export_month` CHAR(7) NOT NULL",
        "`loaded_at_utc` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP",
    ]
    definitions.extend(f"{quote_identifier(header)} {column_type(header)} NULL" for header in headers)
    definitions.extend([
        "PRIMARY KEY (`row_id`)",
        "KEY `idx_export_month` (`export_month`)",
    ])
    if "noticeIdentifier" in headers and "noticeVersion" in headers:
        definitions.append("KEY `idx_notice_version` (`export_month`, `noticeIdentifier`, `noticeVersion`)")
    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {qtable} (" + ", ".join(definitions) + ") "
        "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci"
    )

    cursor.execute(
        "SELECT COLUMN_NAME FROM information_schema.COLUMNS "
        "WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s",
        (database, table),
    )
    existing = {row[0] for row in cursor.fetchall()}
    for header in headers:
        if header not in existing:
            cursor.execute(f"ALTER TABLE {qtable} ADD COLUMN {quote_identifier(header)} {column_type(header)} NULL")


def clear_month(cursor, database: str, export_month: str) -> None:
    cursor.execute(
        "SELECT TABLE_NAME FROM information_schema.TABLES "
        "WHERE TABLE_SCHEMA = %s AND LEFT(TABLE_NAME, 8) = 'doe_raw_'",
        (database,),
    )
    for (table,) in cursor.fetchall():
        cursor.execute(f"DELETE FROM {quote_identifier(table)} WHERE `export_month` = %s", (export_month,))


def load_sources(specs: list[dict], sources: list[tuple[str, TextIO]], export_month: str,
                 host: str, port: int, database: str, user: str, password: str,
                 batch_size: int) -> None:
    try:
        import mysql.connector
    except ImportError as exc:
        raise RuntimeError("Install the dependency with: py -m pip install mysql-connector-python") from exc

    connection = mysql.connector.connect(
        host=host, port=port, user=user, password=password, database=database,
        charset="utf8mb4", use_unicode=True, autocommit=True,
    )
    try:
        cursor = connection.cursor()
        cursor.execute("SET time_zone = '+00:00'")
        for spec in specs:
            ensure_table(cursor, database, spec["table"], spec["headers"])

        connection.autocommit = False
        connection.start_transaction()
        clear_month(cursor, database, export_month)

        spec_by_file = {spec["filename"]: spec for spec in specs}
        total = 0
        for filename, handle in sources:
            spec = spec_by_file[filename]
            qtable = quote_identifier(spec["table"])
            headers = spec["headers"]
            insert_columns = ["export_month", *headers]
            column_sql = ", ".join(quote_identifier(col) for col in insert_columns)
            placeholders = ", ".join(["%s"] * len(insert_columns))
            statement = f"INSERT INTO {qtable} ({column_sql}) VALUES ({placeholders})"
            reader = csv.DictReader(handle)
            batch = []
            loaded = 0
            for row in reader:
                values = [export_month, *(row.get(header, "") for header in headers)]
                batch.append(values)
                if len(batch) >= batch_size:
                    cursor.executemany(statement, batch)
                    loaded += len(batch)
                    batch.clear()
            if batch:
                cursor.executemany(statement, batch)
                loaded += len(batch)
            total += loaded
            print(f"Loaded {loaded:,} rows into {spec['table']}")
            handle.seek(0)
        connection.commit()
        print(f"Completed: {total:,} rows across {len(specs)} DÖE staging tables for {export_month}.")
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="DÖE CSV ZIP file or extracted CSV folder")
    parser.add_argument("--month", required=True, help="Export month in YYYY-MM format")
    parser.add_argument("--database", default="ted_demand_intelligence")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=3306)
    parser.add_argument("--user", default="root")
    parser.add_argument("--batch-size", type=int, default=1000)
    parser.add_argument("--dry-run", action="store_true", help="Validate and summarize files without connecting to MySQL")
    args = parser.parse_args()

    if not re.fullmatch(r"20\d{2}-(0[1-9]|1[0-2])", args.month):
        parser.error("--month must use YYYY-MM format")
    if args.batch_size < 1:
        parser.error("--batch-size must be greater than zero")

    try:
        with open_csv_sources(args.source) as sources:
            specs = inspect_sources(sources)
            print_summary(specs, args.month)
            if args.dry_run:
                print("Dry run only; MySQL was not changed.")
                return 0
            password = getpass.getpass(f"MySQL password for {args.user}@{args.host}: ")
            load_sources(specs, sources, args.month, args.host, args.port,
                         args.database, args.user, password, args.batch_size)
        return 0
    except Exception as exc:
        print(f"DÖE import stopped: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
