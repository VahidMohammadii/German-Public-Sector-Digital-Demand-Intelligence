# Power BI Dashboard Notes

## Purpose and intended users

The report supports exploration of published German procurement notices over time and by category. Its intended users are procurement analysts, public-sector stakeholders, and market researchers interested in patterns in published notices.

## Report pages and visuals

The report contains two pages:

| Page / visual | Analytical question | Measure / interpretation |
|---|---|---|
| **Market Overview — Total Unique Notices** | How many distinct notices are in the selected dataset? | Distinct count of `notice_id`; locally observed total is 1,316,938 with no report filter applied. |
| **TED Notices by Publication Year** | How has publication volume changed over time? | Distinct notices by publication year; 2026 is partial through 29 October. |
| **Top 10 CPV Categories** | Which procurement categories appear most often? | Distinct notices associated with each CPV code/description. A notice may have multiple CPV codes, so category counts can overlap. |
| **Top 10 TED Notice Types** | Which notice types occur most often? | Distinct notices by TED notice-type code, displayed with readable lookup labels. |
| **Time & Contract Analysis — Monthly Notices** | How does notice volume vary by month in a selected year? | Distinct notices by calendar month, with a year slicer. The current 2026 view includes January through October. |
| **Notices by Contract Nature** | How are notices distributed across works, services, and supplies? | Count of distinct notice–nature pairs from the MySQL view. A notice may appear in more than one nature category. |

## Model and counting notes

- The main `notices` table has one row per distinct TED notice in the local model. The KPI uses an explicit distinct-count measure over `notice_id`.
- `notice_cpv_codes` is a notice–CPV bridge. Category analysis counts distinct notice IDs per CPV category rather than summing bridge rows.
- `notice_type_lookup` provides readable labels while retaining each TED notice-type code as a separate category.
- The `notice_contract_natures` MySQL view expands the lot-level JSON field into distinct notice–nature pairs. Repeated lots of the same nature within a notice are counted once in that category.
- Contract-nature categories are not mutually exclusive; their counts should not be added to estimate total unique notices.
- The year slicer filters the report visuals. On the second page, 2026 is selected.

## Coverage and interpretation

The extract covers German buyers from 2016-10-28 through 2026-10-29 inclusive. 2026 is partial. The report counts published TED notices in the stated scope; notice counts are not contract values, expenditure totals, awards, or a complete measure of all German public procurement.

DÖE is planned as a second source for national below-threshold coverage. It is not currently part of the report, so the current pages represent TED only.

## Repository and privacy

The PBIX, populated local database, and connection configuration remain local and are not included in the repository. Selected report screenshots are available in `assets/`. The report notes describe the locally verified state as of 2026-11-16.
