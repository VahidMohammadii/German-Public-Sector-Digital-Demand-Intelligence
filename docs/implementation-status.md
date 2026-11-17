# Implementation Status

**Last updated:** 2026-11-17  
**Overall status:** The TED dataset and two-page report are functional locally. The September 2026 DÖE export has been loaded into local MySQL staging tables. Power Query exploration of selected raw DÖE tables is in progress; cleaning, validation, modeling, and integration with the TED report remain pending. The populated database and PBIX are not committed to this repository.

This log separates work verified on the project owner's Windows laptop from files available in GitHub. Counts below refer to the local database unless explicitly attributed to TED query scope.

## Completed and verified locally

- Created and populated the MySQL schema for TED notices, CPV reference codes, notice-to-CPV links, and ingestion-run tracking.
- Completed TED notice retrieval for the selected Germany/date scope using iteration-token pagination.
- Confirmed the local database contains **1,316,938 distinct TED notices**.
- Connected Power BI Desktop to MySQL.
- Built a two-page TED report with a distinct-notice KPI, annual and monthly trends, top 10 CPV categories, and TED notice types with readable lookup labels.
- Added a year slicer and verified the 2026 monthly view through October.
- Created a MySQL view that expands contract-nature JSON into distinct notice–nature pairs, deduplicating repeated nature values within each notice.
- Added the contract-nature analysis to Power BI and linked the view to the notices table by `notice_id`.
- Formatted the KPI with thousands separators and count labels in thousands for readability.
- Added selected dashboard screenshots to the repository.
- Loaded the September 2026 DÖE monthly export into local MySQL staging tables.
- Connected Power BI Desktop to the local MySQL database and opened the raw DÖE `doe_raw_notice` and `doe_raw_purpose` tables in Power Query for inspection.

## Current query and data coverage

- **TED geography:** buyer country Germany (`buyer-country=DEU`)
- **TED publication dates:** 2016-10-28 through 2026-10-29 inclusive
- **TED API query:** `buyer-country=DEU AND publication-date>=20161028 AND publication-date<20261030`
- **TED operation:** `POST /v3/notices/search`
- **TED pagination:** iteration token; observed page size was 250 notices
- **Local TED database result:** 1,316,938 distinct notices
- **DÖE exploration month:** 2026-09
- **2026 TED coverage:** partial, through 29 October 2026

## DÖE and amount-field review

Exploratory checks in the local MySQL staging data found nonempty amount values in the `purpose` table, with EUR shown as the currency in the reviewed rows. The checks also surfaced zero values and a small number of very large values (including values at or above €1 billion). These are review flags, not confirmed errors or business rules. No rows have been altered or excluded based on these checks.

Procedure-level and lot-level amounts are separate scopes and may coexist for the same procurement. They must not be added together without a source-backed definition. The raw amount and currency fields should be retained while the DÖE source documentation is checked and column-by-column transformations are built in Power Query.

At this point, Power Query has only source/navigation steps for the reviewed raw tables. The September filter and subsequent cleaning/validation steps are still being applied. DÖE has not been joined to TED or included in the report.

## Contract-nature interpretation

The TED `contract_nature` field stores lot-level JSON values. The MySQL view produces one row per distinct `notice_id` and `contract_nature` pair. Each notice is therefore counted once within a nature category, while a notice can contribute to multiple categories.

## Sources and next stages

- **TED:** primary source for the current loaded dataset and report.
- **DÖE:** September 2026 export is staged locally; Power Query ETL and field-level validation are underway. Integration into the analytical model is future work.
- **Repository code:** committed SQL is a starter schema. Reusable ingestion code and sanitized setup instructions are planned deliverables.

## Data handling

Credentials, access tokens, continuation tokens, checkpoint files, the populated local database, and raw bulk export files are excluded from the repository. The Power BI report file remains local; selected screenshots and report documentation provide a reviewable overview of the current TED dashboard.
