# Power BI Dashboard Notes

## Purpose and intended users

The report supports exploration of published German procurement notices over time and by category. Its intended users are procurement analysts, public-sector stakeholders, and market researchers interested in patterns in published notices.

The report should use a small set of readable visuals that answer explicit analytical questions, with data scope and measure definitions visible.

## Current local report

The Power BI Desktop report connects to the local MySQL database. Its current visuals include:

| Visual | Analytical question | Measure / interpretation |
|---|---|---|
| Total notice card | How many notices are in the selected dataset? | Distinct count of `notice_id` from the notice table; locally observed total is 1,316,938 with no report filter applied. |
| Top 10 CPV categories | Which procurement categories appear most often? | Distinct notices associated with each CPV code/description. A notice may have multiple CPV codes, so category counts can overlap. |
| Annual publication trend | How has the number of published notices changed by year? | Distinct notices by publication year. |
| TED notice types | Which notice types occur most often? | Distinct notices by TED notice-type code, with a separate lookup table providing readable labels. |
| Monthly trend with year slicer | How does notice volume vary by month in a selected year? | Distinct notices by calendar month, filtered to a selected year. The 2026 view currently has data through October. |

These are prototype report visuals, not a claim that every analytical field has been normalized. The extract covers German buyers from 2016-10-28 through 2026-10-29 inclusive; 2026 is partial.

## Counting and model notes

- The main `notices` table has one row per distinct TED notice in the local model, so distinct notice count is the report's primary volume measure.
- `notice_cpv_codes` is a many-to-many bridge at notice–CPV level. Summing its rows is not the same as counting notices; category analysis should count distinct notice IDs per CPV category.
- TED notice-type codes are not merged merely because their names look similar. The lookup labels preserve each official code as a separate category.
- Month names are displayed in calendar order. The year slicer selects the annual context for the monthly trend.

## Contract-nature analysis: planned

The source `contract_nature` field contains JSON arrays because values can occur at lot level. For analysis, the values need to be standardized into distinct notice–nature pairs so an individual notice is counted once within each category.

A MySQL view is planned to provide this normalized dataset. After creating it, the results and filter behavior will be validated before adding a contract-nature visual.

## Interpretation and coverage

This report counts published notices in TED for the stated query scope. Notice counts are not contract values, expenditure totals, awards, or a complete measure of all German public procurement. DÖE is a planned second source for national and below-threshold coverage; it is not currently part of this report.

## Repository and privacy

The PBIX, populated local database, API checkpoint/token, and credentials remain local and are not included in the repository. The report notes here describe the locally verified state as of 2026-11-14.
