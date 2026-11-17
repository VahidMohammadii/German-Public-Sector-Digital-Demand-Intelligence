# DÖE Staging and Power Query Status

**Status date:** 2026-11-17  
**Scope in progress:** September 2026 local DÖE export

## Current state

- The monthly DÖE CSV export is loaded into local MySQL raw staging tables.
- Power BI Desktop connects to the local MySQL instance.
- The raw `doe_raw_notice` and `doe_raw_purpose` tables are open in Power Query for inspection.
- The reviewed queries currently show only source and navigation steps. The user is applying the `export_month = 2026-09` filter before continuing with column-by-column profiling and ETL.
- DÖE remains separate from TED and has not been integrated into the analytical model or report.

The raw source tables remain the traceable input. Power Query changes should be documented as explicit steps; do not overwrite or silently modify the raw source.

## Exploratory amount checks

Local SQL checks on the staged September data found:

- Nonempty `estimatedValue` entries in the DÖE `purpose` table were reported with currency EUR in the reviewed records.
- Some rows contain zero or zero-decimal values.
- A small number of rows have exceptionally large values, including values at or above €1 billion.
- Amounts exist at both procedure and lot scope.

These are signals to investigate, not confirmed errors. No amount has been removed, capped, imputed, converted, or otherwise changed based on these checks. The currency finding applies to the reviewed staged data and should be revalidated in Power Query before use.

Procedure-level and lot-level values can represent different scopes for a procurement. Do not sum the two scopes together unless the source documentation establishes that this is valid. Preserve the raw amount, currency, scope, notice/version, and lot identifiers through validation.

## Planned Power Query review

For the September slice, inspect each field and record:

1. source column and data type;
2. null, blank, and distinct-value counts;
3. invalid or unexpected formats;
4. key behavior, including notice identifier plus version and lot identifier where applicable;
5. amount scope and currency consistency;
6. transformation rule, reason, and resulting row counts.

Keep raw values available alongside any standardized columns. Convert amounts to a numeric type only after validating formats and locale behavior. If currencies other than EUR are found, retain the original amount and currency and apply a documented conversion source/date before creating a standardized EUR measure. Do not assume all values are EUR from a partial preview.

Potential zero and high-value records should be traced to their source notices or official field definitions before deciding how to treat them. Until then, flag them for review and preserve them.

## Integration gate

DÖE should be added to the report model only after the monthly slice has documented source coverage, key and duplicate behavior, field definitions, and validated transformations. Any TED/DÖE overlap should be measured with source-aware keys rather than removed on a guessed identifier match.

See [implementation status](implementation-status.md) for the project-wide progress and [data-source register](data-sources.md) for source coverage.
