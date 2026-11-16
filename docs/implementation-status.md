# Implementation Status

**Last updated:** 2026-11-16  
**Overall status:** TED historical dataset loaded locally; the two-page Power BI report is functional, including normalized contract-nature analysis. DÖE integration and publication of reusable ingestion code remain future work. The populated database and PBIX are not committed to this repository.

This log separates work verified on the project owner's Windows laptop from files available in GitHub. Counts below refer to the local database unless explicitly attributed to TED query scope.

## Completed and verified locally

- Created and populated the MySQL schema for notices, CPV reference codes, notice-to-CPV links, and ingestion-run tracking.
- Completed TED notice retrieval for the selected Germany/date scope using iteration-token pagination.
- Confirmed the local database contains **1,316,938 distinct notices**.
- Connected Power BI Desktop to MySQL.
- Built a two-page report with a distinct-notice KPI, annual and monthly trends, top 10 CPV categories, and TED notice types with readable lookup labels.
- Added a year slicer and verified the 2026 monthly view through October.
- Created a MySQL view that expands contract-nature JSON into distinct notice–nature pairs, deduplicating repeated nature values within each notice.
- Added the contract-nature analysis to Power BI and linked the view to the notices table by `notice_id`.
- Formatted the KPI with thousands separators and count labels in thousands for readability.
- Added selected dashboard screenshots to the repository.

## Current query and data coverage

- **Geography:** buyer country Germany (`buyer-country=DEU`)
- **Publication dates:** 2016-10-28 through 2026-10-29 inclusive
- **API query:** `buyer-country=DEU AND publication-date>=20161028 AND publication-date<20261030`
- **TED operation:** `POST /v3/notices/search`
- **Pagination:** iteration token; observed page size was 250 notices
- **Local database result:** 1,316,938 distinct notices
- **2026 coverage:** partial, through 29 October 2026

## Contract-nature interpretation

The TED `contract_nature` field stores lot-level JSON values. The MySQL view produces one row per distinct `notice_id` and `contract_nature` pair. Each notice is therefore counted once within a nature category, while a notice can contribute to multiple categories.

## Sources and next stages

- **TED:** primary source for the current loaded dataset and report.
- **DÖE:** planned second source for German below-threshold procurement notices. Acquisition, schema mapping, deduplication, and integration are future work.
- **Repository code:** committed SQL is a starter schema. Reusable ingestion code and sanitized setup instructions are planned deliverables.

## Data handling

Credentials, access tokens, continuation tokens, checkpoint files, and the populated local database are excluded from the repository. The Power BI report file remains local; selected screenshots and report documentation provide a reviewable overview of the current dashboard.
