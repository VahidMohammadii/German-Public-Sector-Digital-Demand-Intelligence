# Data Source Register

## Primary source: Tenders Electronic Daily (TED)

| Field | Current value |
|---|---|
| Source | Tenders Electronic Daily (TED), the EU public procurement notices service |
| Access | TED public API, `POST /v3/notices/search` |
| Query scope | Buyers in Germany; publication dates 2016-10-28 through 2026-10-29 inclusive |
| Query | `buyer-country=DEU AND publication-date>=20161028 AND publication-date<20261030` |
| Records | Published notices |
| Local database | 1,316,938 distinct notice records |
| Pagination | Iteration-token mode; observed page size 250 |
| Documentation | [TED Developer Portal](https://docs.ted.europa.eu/) · [TED API documentation](https://docs.ted.europa.eu/api/latest/index.html) |

The date range describes the current local extract; 2026 coverage is partial through 29 October. A future project update can add another period by retrieving the expanded range.

## Secondary source under evaluation: Datenservice Öffentlicher Einkauf (DÖE)

The September 2026 DÖE monthly export has been loaded into local MySQL staging tables. Selected raw tables (`doe_raw_notice` and `doe_raw_purpose`) are being inspected in Power Query. This is a local staging and ETL preparation step; DÖE has not been joined to TED or included in the Power BI analytical report.

Before integration, document the export's exact scope, publication-date coverage, identifiers, licensing and attribution, and define source-aware duplicate handling. Preserve the raw fields and source provenance during transformation. See [DÖE staging and Power Query status](doe-staging-and-power-query.md).

## Selected fields and reference data

The initial TED field set includes publication number and date, notice type, title, buyer, country, CPV classification, and tender deadline. The local MySQL model also tracks notice-to-CPV associations and ingestion runs. Field mappings should be confirmed against the committed schema and representative source records as the reusable ingestion code is packaged.

The local setup includes CPV reference descriptions retrieved from TED reference material. Reference version and retrieval details should be recorded if the list is distributed with the project.

## Coverage notes

- TED represents notices published through TED for the selected query and period.
- A notice count is not equivalent to total procurement value or all purchasing by German public bodies.
- Award information may be absent or not linkable to an original notice.
- Buyer, supplier, CPV, and geographic fields may be missing or inconsistent.
- The current TED extract ends on 2026-10-29; the 2026 annual value is therefore partial.
- DÖE coverage and overlap with TED have not yet been quantified for the staged month.

## Data handling and reuse

Do not commit credentials, continuation tokens, checkpoint files, the populated database, or the raw monthly export. Review the sources' current terms and attribution requirements before redistributing downloaded records. The repository contains documentation and starter SQL, not a bulk extract.
