# German Public-Sector Digital Demand Intelligence

A portfolio analytics project exploring published public procurement demand in Germany, with an initial focus on digital-service opportunities. It combines TED notice data, a Python ingestion workflow, a MySQL relational model, and an interactive Power BI report.

## Project question

**How can published procurement notices help identify recurring buyers, categories, and changes in Germany's public-sector digital-service demand?**

## Purpose and intended use

This project examines published procurement notices to make patterns in buyers, categories, and publication timing easier to explore. The report is intended for analysts and public-sector stakeholders interested in Germany's published procurement demand. It makes the data scope, measure definitions, and source coverage explicit.

## Current results

- **TED scope:** German buyers; publication dates from **2016-10-28 through 2026-10-29** (inclusive).
- **Loaded dataset:** **1,316,938 distinct notices** in the local MySQL database.
- **Dashboard:** Power BI Desktop is connected to MySQL. Current report visuals include total distinct notices, top 10 CPV categories, annual publication trend, TED notice types with readable labels, and a monthly trend that can be filtered by year.
- **Time coverage:** 2026 is partial through 29 October. The documented range can be extended later by retrieving another period.
- **Contract nature:** TED's contract-nature field is stored as JSON arrays and may repeat values across lots. A Power Query normalization preview produced works/services/supplies rows, but applying the query failed with an OLE DB/ODBC expression error. It is not in the validated report yet. The next planned route is a MySQL view, followed by validation before adding a visualization.
- **Next source:** Germany's Datenservice Öffentlicher Einkauf (DÖE) is planned as a second source for below-threshold notices; it has not yet been integrated.
- **Repository contents:** reusable starter SQL and project documentation are committed. The working ingestion script, populated database, and Power BI report remain local and are not included in this repository yet.

See the [Power BI dashboard notes](docs/powerbi-dashboard.md) and [implementation status](docs/implementation-status.md) for details.

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

- `docs/`: project scope, architecture, data sources, dashboard notes, and implementation status
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
- [Power BI dashboard notes](docs/powerbi-dashboard.md)
