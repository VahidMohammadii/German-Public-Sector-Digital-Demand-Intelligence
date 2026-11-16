import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("load_monthly_export.py")
SPEC = importlib.util.spec_from_file_location("doe_loader", SCRIPT)
doe_loader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(doe_loader)


class DÖELoaderTests(unittest.TestCase):
    def test_table_names_are_source_prefixed_and_snake_case(self):
        self.assertEqual(doe_loader.table_name("notice.csv"), "doe_raw_notice")
        self.assertEqual(doe_loader.table_name("noticeResult.csv"), "doe_raw_notice_result")

    def test_sql_identifiers_reject_unsafe_names(self):
        with self.assertRaises(ValueError):
            doe_loader.quote_identifier("notice; DROP TABLE notices")

    def test_inspection_counts_versions_and_distinct_notices(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / "notice.csv").write_text(
                "noticeIdentifier,noticeVersion,procedureLegalBasis,publicationDate\n"
                "n-1,01,de-uvgo,2026-09-01T00:00:00+02:00\n"
                "n-1,02,,2026-09-20T00:00:00+02:00\n"
                "n-2,01,de-vob,2026-09-21T00:00:00+02:00\n",
                encoding="utf-8",
            )
            with doe_loader.open_csv_sources(folder) as sources:
                specs = doe_loader.inspect_sources(sources)
            notice = specs[0]
            self.assertEqual(notice["row_count"], 3)
            self.assertEqual(len(notice["notice_keys"]), 3)
            self.assertEqual(len(notice["notice_ids"]), 2)
            self.assertEqual(notice["legal_basis"]["[blank]"], 1)

    def test_inspection_rejects_duplicate_headers(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            (folder / "notice.csv").write_text(
                "noticeIdentifier,noticeIdentifier\nn-1,n-1\n", encoding="utf-8"
            )
            with doe_loader.open_csv_sources(folder) as sources:
                with self.assertRaises(ValueError):
                    doe_loader.inspect_sources(sources)


if __name__ == "__main__":
    unittest.main()
