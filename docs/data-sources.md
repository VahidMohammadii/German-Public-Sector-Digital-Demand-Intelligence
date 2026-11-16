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

## Second source: Datenservice Öffentlicher Einkauf (DÖE)

| Field | Current value |
|---|---|
| Source | DÖE Publication Service Open Data API |
| Access | `GET /api/notice-exports` with `pubMonth` and `format=csv.zip` |
| Pilot period | September 2026 |
| Pilot profile | 19 normalized CSV tables; 477,492 rows; 23,517 notice versions and 23,357 distinct notice identifiers |
| Version key | `noticeIdentifier` + `noticeVersion` |
| Staging design | Loader creates separate `doe_raw_*` tables in the local MySQL schema |
| Documentation | [Open Data API](https://oeffentlichevergabe.de/documentation/swagger-ui/opendata/index.html#/opendata/getExportAsEforms) · [Publication policy](https://oeffentlichevergabe.de/ui/de/publicationPolicy) |

The monthly export contains all notice versions published in that month, so the DÖE source is not limited to below-threshold notices. Threshold classification and cross-source deduplication are defined in the analytical layer after reviewing legal-basis and notice-type fields. The September pilot includes 2,568 notice versions without `procedureLegalBasis`; these remain unclassified until the mapping is documented. Raw CSV exports remain local and are not committed.

## Selected fields and reference data

The TED field set includes publication number and date, notice type, title, buyer, country, CPV classification, and tender deadline. The local MySQL model also tracks notice-to-CPV associations and ingestion runs. DÖE pilot field selections and version-aware joins are documented in [the DÖE pilot note](doe-pilot.md).

The local setup includes CPV reference descriptions retrieved from TED reference material. Reference version and retrieval details should be recorded if the list is distributed with the project.

## Coverage notes

- TED represents notices published through TED for the selected query and period.
- A notice count is not equivalent to total procurement value or all purchasing by German public bodies.
- Award information may be absent or not linkable to an original notice.
- Buyer, supplier, CPV, and geographic fields may be missing or inconsistent.
- The current extract ends on 2026-10-29; the 2026 annual value is therefore partial.

## Data handling and reuse

Do not commit credentials, continuation tokens, checkpoint files, or the populated database. Review the source's current terms and attribution requirements before redistributing downloaded records. The repository contains documentation and starter SQL, not a bulk extract.
