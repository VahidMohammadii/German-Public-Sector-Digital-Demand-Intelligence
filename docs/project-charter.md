# Project Charter

## Working title

**German Public-Sector Digital Demand Intelligence**

## Problem statement

Organizations considering public-sector digital services need a structured way to explore visible procurement demand, recurring buyers, geographic patterns, and award evidence. Public notices are fragmented across records and may contain incomplete or differently structured fields. A repeatable data workflow can make those patterns easier to inspect and discuss.

## Project question

**How can published TED notices and contract award information be used to identify and prioritize public-sector digital-service market opportunities in Germany for further commercial assessment?**

## Objective

Design and implement a modular analytical workflow that collects a defined set of TED notices, validates and standardizes them, stores them for SQL analysis, and presents interpretable demand indicators in Power BI.

The output supports **prioritization for further review**, not an automated market-entry or bid/no-bid decision.

## Intended users

- Business development professionals
- Product and market strategy teams
- Analysts exploring public procurement demand

## Initial scope

- Public TED notices relevant to selected digital-service categories
- Related award notices where available and linkable
- Buyer, time, geography, CPV, and award fields supported by the source
- Data retrieval, quality checks, transformation, analytical storage, metrics, and dashboard design
- Documentation of query scope, assumptions, limitations, and refresh behavior

## Out of scope for the first version

- All German public procurement, including purchases not published in TED
- Private-sector demand
- Forecasts of revenue, profitability, or bid success
- Automated legal eligibility assessments
- An always-on production service before hosting and operational requirements are defined

## Planned questions and indicators

| Question | Candidate indicator | Important qualification |
|---|---|---|
| Is published demand changing? | Notice count by publication period | Depends on query scope and source coverage |
| Which categories recur? | Notice count by selected CPV category | Classification rules must be documented |
| Which buyers publish repeatedly? | Distinct notices by buyer | Buyer names and identifiers may vary |
| Where is demand published? | Notice count by NUTS/geographic field | Location may be absent or refer to different entities |
| What is known about awards? | Award count and reported award value | Award records and values may be incomplete |
| What merits further review? | Transparent, documented ranking criteria | A ranking is a screening aid, not proof of opportunity |

Metric definitions will be finalized after profiling the API fields and sample data.

## Deliverables

1. Reproducible TED data-collection code and configuration examples
2. Data-quality and transformation rules
3. SQL schema and analytical queries
4. Power BI dashboard with documented measures
5. Management summary that distinguishes observations from interpretation
6. Source, refresh, and limitation documentation

## Success criteria

- A reviewer can understand the question, scope, and data limitations from the repository.
- The collection process documents its query parameters and retrieval time.
- Data validation identifies missing, duplicate, malformed, or inconsistent records.
- Analytical measures have explicit definitions and can be traced to source fields.
- The dashboard separates notices from awards and communicates incomplete coverage.
- Results can be reproduced from the documented process without committing secrets.

## Data and inference boundaries

TED records show published procurement information available through TED. They do not establish the full volume of German public or private demand. Missing values must remain distinguishable from true zero values. Associations and historical counts do not establish causation, future demand, profitability, or bid success.

## Project ownership and AI assistance

I own the project scope, implementation choices, execution of the tools, interpretation of results, and final decisions. AI may assist with design, troubleshooting, testing, and documentation. Any AI-assisted analysis will be checked against the source data and documented where relevant.

## Status

Local implementation has started: the TED query has been validated, the MySQL schema and one-notice ingestion test have been checked, and historical ingestion is in progress. The working script and database schema have not yet been added to this repository. Power BI remains planned. See [Implementation Status](implementation-status.md).
