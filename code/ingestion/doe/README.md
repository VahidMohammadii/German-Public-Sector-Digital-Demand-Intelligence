# DÖE monthly CSV loader

This loader places the normalized CSV tables from a DÖE monthly export into source-specific MySQL staging tables. It preserves each published notice version and keeps the original DÖE columns available for later transformations.

## Requirements

- Python 3.9 or newer
- MySQL Connector/Python
- A local MySQL schema, such as the project's existing `ted_demand_intelligence` schema

Install the connector once from Command Prompt or PowerShell:

```powershell
py -m pip install mysql-connector-python
```

## Validate the September 2026 pilot

The official DÖE export can be supplied as a ZIP file or as a folder containing its extracted CSV files. A dry run validates the files and reports counts without connecting to MySQL:

```powershell
py code/ingestion/doe/load_monthly_export.py "C:\path\to\2026-09.csv.zip" --month 2026-09 --dry-run
```

To import the export, remove `--dry-run`:

```powershell
py code/ingestion/doe/load_monthly_export.py "C:\path\to\2026-09.csv.zip" --month 2026-09 --database ted_demand_intelligence --user root
```

The script prompts for the MySQL password; it is not stored in the command, a file, or the repository. Host and port default to `127.0.0.1` and `3306`.

## Staging design

- Each source CSV becomes a separate table named `doe_raw_<file_name>`, for example `notice.csv` becomes `doe_raw_notice` and `noticeResult.csv` becomes `doe_raw_notice_result`.
- Tables contain `row_id`, `export_month`, and `loaded_at_utc`, followed by the CSV's original columns. Source values are retained as text in this landing layer; identifier columns use bounded string types.
- A composite index on `export_month`, `noticeIdentifier`, and `noticeVersion` supports version-aware joins. The surrogate `row_id` preserves every source row without collapsing repeats.
- Re-running an import replaces only that export month in the DÖE staging tables. Other months and all TED tables are left intact.
- The staging layer does not apply a threshold classification, select a latest version, or merge DÖE identifiers with TED identifiers. Those steps belong in the reviewed analytical layer.

Do not commit downloaded CSV exports, database credentials, or populated local database files.

## Official source

[DÖE Open Data API documentation](https://oeffentlichevergabe.de/documentation/swagger-ui/opendata/index.html#/opendata/getExportAsEforms) documents the `GET /api/notice-exports` endpoint and its `pubMonth` parameter.
