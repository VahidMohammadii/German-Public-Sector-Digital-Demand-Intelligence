# DÖE monthly export pilot

## Pilot profile

The September 2026 CSV export contains 19 normalized tables and 477,492 rows across those tables. Its `notice.csv` table contains 23,517 notice versions associated with 23,357 distinct notice identifiers. Some notices have multiple versions in the selected month, so analyses must use a version-aware key and choose the appropriate grain for each measure.

## Fields for the first analytical model

| Source table | Relevant fields | Initial use |
|---|---|---|
| `notice.csv` | `noticeIdentifier`, `noticeVersion`, `procedureLegalBasis`, `formType`, `noticeType`, `publicationDate` | Notice-version key, publication time, legal-basis and notice-type review |
| `purpose.csv` | `noticeIdentifier`, `noticeVersion`, `lotIdentifier`, `mainNature`, `title`, `estimatedValue`, `estimatedValueCurrency` | Lot-level purpose, title, nature, and estimated value |
| `classification.csv` | `noticeIdentifier`, `noticeVersion`, `lotIdentifier`, `classificationType`, `mainClassificationCode`, `additionalClassificationCodes` | Notice- and lot-level CPV classification |
| `organisation.csv` | `noticeIdentifier`, `noticeVersion`, `organisationName`, `organisationIdentifier`, `organisationRole`, `buyerLegalType` | Buyer and other organization roles |
| `lot.csv` | `noticeIdentifier`, `noticeVersion`, `lotIdentifier` | Lot relationships |
| `placeOfPerformance.csv` | `noticeIdentifier`, `noticeVersion`, `lotIdentifier`, `placePerformanceCountrySubdivision`, `placePerformanceCountryCode` | Performance geography |
| `procedure.csv` | `noticeIdentifier`, `noticeVersion`, `procedureType`, `procedureFeatures` | Procedure context |

The remaining CSV tables are retained in the raw landing layer so later analysis can use result, contract, duration, submission, and strategic-procurement details without repeating acquisition.

## Modeling decisions

- The natural notice-version key is `(noticeIdentifier, noticeVersion)`; `noticeIdentifier` alone identifies a notice across its versions.
- Related rows are joined using that composite key, plus `lotIdentifier` where the relationship is lot-level. Some classifications are defined at notice level and have no lot identifier.
- Raw DÖE tables use the `doe_raw_` prefix in the existing MySQL schema. TED tables remain separate.
- The monthly load is idempotent by `export_month`; reloading a month replaces that month's DÖE staging rows.
- Threshold status is not assigned during raw ingestion. In the pilot, 2,568 notice versions have no `procedureLegalBasis`; legal-basis and notice-type rules must be reviewed before the below-threshold comparison is built.
- Cross-source deduplication is deferred to the shared analytical layer and must not rely on equality between TED and DÖE identifiers.

## Source notes

The DÖE Open Data endpoint returns all notice versions published in the requested month. Its CSV export represents one-to-many notice relationships in separate tables. The official documentation describes the CSV mapping, stable existing column names, and notice-version key.

- [DÖE Open Data API](https://oeffentlichevergabe.de/documentation/swagger-ui/opendata/index.html#/opendata/getExportAsEforms)
- [DÖE publication policy and Open Data access](https://oeffentlichevergabe.de/ui/de/publicationPolicy)

The downloaded export is kept locally and is not part of the repository.
