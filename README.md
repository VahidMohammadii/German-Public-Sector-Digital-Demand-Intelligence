# German Public-Sector Digital Demand Intelligence

A portfolio project to explore published demand for digital services in Germany's public sector using notices and award information from Tenders Electronic Daily (TED).

> **Project status:** Foundation and design. The data pipeline, SQL database, and Power BI dashboard have not yet been implemented.

## Project question

**How can published TED notices and contract award information be used to identify and prioritize public-sector digital-service market opportunities in Germany for further commercial assessment?**

## Purpose

The project is planned as a modular, reproducible analytics workflow that will:

- collect relevant TED notices and, where available, their award information;
- preserve source records and document retrieval time and query scope;
- validate and standardize records before analytical use;
- store structured data for repeatable SQL analysis;
- present demand patterns and documented indicators in Power BI;
- summarize opportunities for further business review, including data limitations.

The intended audience is business development, product, and market-analysis professionals.

## Planned analytical questions

- How does the volume of relevant published notices change over time?
- Which public buyers, regions, and digital-service categories appear most often?
- How frequently do buyers publish relevant opportunities?
- Where award information is available, what can it tell us about awarded contracts and suppliers?
- Which categories merit further commercial assessment, and what evidence supports that prioritization?

The project will distinguish notices from awards. Missing award values or incomplete records will not be treated as zero.

## Planned workflow

`TED notices and award notices → ingestion → validation and standardization → SQL analytical model → metrics → Power BI → commercial review`

The workflow is a design target; it does not imply that these components are already operational.

## Repository map

| Path | Purpose |
|---|---|
| `docs/` | Project scope, architecture, and source documentation |
| `code/ingestion/` | Planned TED API collection components |
| `code/data_quality/` | Planned validation and quality checks |
| `code/transformations/` | Planned normalization and classification |
| `code/database/` | Planned SQL schema and loading logic |
| `code/analytics/` | Planned analytical queries and metric definitions |
| `code/orchestration/` | Planned pipeline configuration and execution |
| `powerbi/` | Planned Power BI deliverables and selected screenshots |
| `data/` | Local-only data workspace; raw or sensitive extracts should not be committed |

Folders and components will be added as implementation begins. Git does not retain empty directories.

## Data and scope

The planned primary source is TED's public procurement notices and related award notices. TED represents published notices available through its service; it is not a complete census of all public purchasing in Germany and does not represent private-sector demand. Coverage and field completeness must be assessed and documented.

This analysis can describe patterns in the observed TED data and help prioritize questions for further review. It cannot, by itself, establish total market size, supplier profitability, or the likelihood that a specific bid will succeed.

See [the source register](docs/data-sources.md) and [project charter](docs/project-charter.md).

## Reproducibility and updates

The intended ingestion process will record its query scope, retrieval timestamp, and run outcome. New records can be appended or reconciled in storage, after which the analytical model and Power BI dataset can be refreshed. Scheduled and hosted refresh will depend on the final deployment environment and the applicable Power BI configuration.

API behavior and schemas can change. The implementation should isolate the TED connector, validate incoming fields, log failures, and document the last successful retrieval.

## Data handling

- Do not commit credentials, access tokens, or personal secrets.
- Do not commit raw bulk extracts unless licensing, size, and privacy have been reviewed.
- Keep local data and environment-specific settings out of version control.
- Use synthetic or appropriately small public samples for examples.

## Current status and next steps

1. Confirm the initial TED query scope and relevant digital-service categories.
2. Review the TED API documentation and record the selected endpoints and fields.
3. Define a small, reproducible extraction sample.
4. Specify data-quality rules and the initial SQL model.
5. Implement ingestion and validation before building dashboard measures.

No completed analysis or dashboard results are claimed at this stage.

## License

A license has not yet been selected. Until one is added, reuse rights for this repository's original materials are not granted by default. Source data remains subject to TED and applicable data-use terms.
