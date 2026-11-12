# German Public-Sector Digital Demand Intelligence

A portfolio analytics project exploring published public procurement demand in Germany, with an initial focus on digital-service opportunities. It combines TED notice data, a Python ingestion workflow, a MySQL relational model, and a Power BI report.

## Project question

**How can published procurement notices help identify recurring buyers, categories, and changes in Germany's public-sector digital-service demand?**

## Current results

- **TED scope:** German buyers; publication dates from **2016-10-28 through 2026-10-29** (inclusive).
- **Loaded dataset:** **1,316,938 distinct notices** in the local MySQL database.
- **Dashboard:** Power BI Desktop is connected to MySQL and currently shows unique notice count, the top 10 CPV categories, annual publication trend, and top 10 TED notice-type codes.
- **Time coverage:** 2026 is partial through 29 October. The documented range can be extended later by retrieving another period.
- **Next source:** Germany's Datenservice Öffentlicher Einkauf (DÖE) is planned as a second source for below-threshold notices; it has not yet been integrated.
- **Repository contents:** reusable starter SQL and project documentation are committed. The working ingestion script, populated database, and Power BI report remain local and are not included in this repository yet.

## Data flow

`TED API → Python → MySQL → Power BI Desktop`

Python retrieves TED notices using iteration-token pagination and loads structured data into MySQL. MySQL stores notices, CPV classifications, and ingestion-run metadata. Power BI connects to the relational model for interactive analysis.

## Skills demonstrated

- Public API data retrieval and token-based pagination
- Python data processing and MySQL Connector
- Relational schema design, keys, and SQL
- Power BI data modeling, filtering, and time-series reporting
- Source documentation, data coverage, and reproducible project communication

## Repository guide

- `docs/`: project scope, architecture, data sources, and implementation status
- `code/database/schema/`: starter MySQL schema
- `code/analytics/metrics/`: draft metric definitions
- `powerbi/`: report and screenshot documentation; the PBIX is currently local
- `data/`: local workspace guidance; raw bulk data is not committed

## Reproducibility and data handling

The local database and Power BI file depend on the owner's Windows setup. Credentials, API continuation tokens, checkpoint files, and the bulk extract are intentionally excluded. Setup instructions and sanitized, reusable ingestion code are the next repository deliverables.

TED records represent published notices available in the selected source and query scope. The notice count is a count of distinct notice records, not a measure of contract value or total German public procurement.

## Sources and reuse

TED is the primary source for the current analysis. DÖE is a planned addition for national below-threshold coverage. Review the [data-source register](docs/data-sources.md) for source links, scope, and data-handling notes. Source data terms and attribution requirements should be checked before redistribution; this repository does not include the downloaded bulk data.

## Project documentation

- [Architecture](docs/architecture.md)
- [Implementation status](docs/implementation-status.md)
- [Project charter](docs/project-charter.md)
- [Data sources](docs/data-sources.md)

