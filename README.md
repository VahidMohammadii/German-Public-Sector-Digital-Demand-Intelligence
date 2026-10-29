# German Public-Sector Digital Demand Intelligence

A portfolio project exploring published demand for digital services in Germany's public sector using notices from Tenders Electronic Daily (TED).

> **Project status (2026-10-29):** Local proof of concept. The TED query, Python-to-MySQL connection, database schema, and one-notice test have been verified. The historical TED retrieval is still in progress. Power BI is not connected yet. See [Implementation Status](docs/implementation-status.md).

## Project question

**How can published TED notices and contract award information be used to identify and prioritize public-sector digital-service market opportunities in Germany for further commercial assessment?**

## Purpose

The project is being developed as a modular analytics workflow to:

- collect relevant TED notices and, where available, their award information;
- preserve source identifiers and retrieval-run metadata;
- validate and standardize records before analysis;
- store structured data for repeatable SQL analysis;
- present documented indicators in Power BI;
- support opportunity screening for further commercial review.

The intended audience is business development, product, and market-analysis professionals.

## Planned analytical questions

- How does the volume of relevant published notices change over time?
- Which public buyers, regions, and digital-service categories appear most often?
- How frequently do buyers publish relevant opportunities?
- Where award information is available, what can it tell us about awarded contracts and suppliers?
- Which categories merit further commercial assessment, and what evidence supports that prioritization?

The project distinguishes notices from awards. Missing award values or incomplete records are not treated as zero.

## Workflow

`TED Search API → Python ingestion and transformation → MySQL → Power BI`

Python requests TED notices page by page using an iteration token, prepares fields, and writes records to the local MySQL database. MySQL stores notices, CPV classifications, and ingestion-run metadata. Power BI is the planned reporting layer and has not been connected yet.

The current script and SQL setup are local working materials and have not yet been committed to this repository. The [implementation-status log](docs/implementation-status.md) separates verified local progress from repository deliverables.

## Repository map

| Path | Purpose |
|---|---|
| `docs/` | Project scope, architecture, source documentation, and implementation status |
| `code/ingestion/` | Planned TED API collection components |
| `code/data_quality/` | Planned validation and quality checks |
| `code/transformations/` | Planned normalization and classification |
| `code/database/` | Planned SQL schema and loading logic |
| `code/analytics/` | Planned analytical queries and metric definitions |
| `code/orchestration/` | Planned pipeline configuration and execution |
| `powerbi/` | Planned Power BI deliverables and selected screenshots |
| `data/` | Local-only data workspace; raw or sensitive extracts should not be committed |

## Data and scope

The current test uses TED's public notices API for buyers in Germany and publication dates from 2016-10-28 through 2026-10-29. TED reported 1,316,938 matching notices during query validation; the full retrieval is incomplete. TED represents published notices available through its service, not all public purchasing in Germany or private-sector demand.

See [the source register](docs/data-sources.md), [project charter](docs/project-charter.md), and [implementation status](docs/implementation-status.md).

## Data handling

- Do not commit credentials, access tokens, or personal secrets.
- Do not commit checkpoint files or continuation tokens.
- Do not commit raw bulk extracts unless licensing, size, and privacy have been reviewed.
- Keep local data and environment-specific settings out of version control.
- Use small, appropriately attributed public samples for examples.

## License

A license has not yet been selected. Until one is added, reuse rights for this repository's original materials are not granted by default. Source data remains subject to TED and applicable data-use terms.
