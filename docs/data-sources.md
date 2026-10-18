# Data Source Register

## Primary source: Tenders Electronic Daily (TED)

| Field | Planned value |
|---|---|
| Source | Tenders Electronic Daily (TED), the EU public procurement notices service |
| Planned access | TED public API, subject to endpoint and usage verification |
| Intended records | Relevant notices and related award information where available |
| Geographic focus | Germany, based on documented query and notice fields |
| Planned use | Describe published demand patterns and support opportunity screening |
| Current status | Source selected; extraction and field coverage not yet verified |
| Documentation | [TED Developer Portal](https://docs.ted.europa.eu/) |
| API reference | [TED API documentation](https://docs.ted.europa.eu/api/latest/index.html) |

## Planned extraction documentation

Before implementation, record:

- exact API endpoint and API version;
- query syntax and included notice types;
- date range and publication-date semantics;
- country, CPV, and other filters;
- pagination and rate-limit behavior;
- fields requested and fields actually returned;
- retrieval timestamp and number of records;
- any known exclusions or failed requests.

## Candidate fields to profile

The final field list depends on the selected TED operation and actual response schema. Candidate areas include:

- notice identifiers and notice type;
- publication date and deadline;
- contracting authority or buyer identifiers and names;
- CPV codes and descriptions;
- place of performance and NUTS identifiers;
- procurement procedure and status;
- links between original notices and award notices;
- reported award value and currency;
- awarded supplier information, where published.

Do not assume every field is present or consistent across notice types.

## Reference data

CPV and NUTS classifications may be used to make categories and geography easier to interpret. The exact source, version, retrieval date, and applicable reuse terms should be recorded when reference datasets are selected.

## Coverage and interpretation limits

- TED contains published notices available through the service, not every purchase made by every German public body.
- The analysis will depend on the selected query, date range, notice types, and available fields.
- Award notices may be missing, delayed, or not linkable to an original notice.
- Reported award values can use different currencies or value definitions and may be absent.
- Buyer, supplier, CPV, and geography fields can be incomplete or inconsistent.
- Notice counts are not equivalent to total addressable market, revenue, or realized expenditure.
- Historical patterns cannot establish future demand, profitability, or bid success.

## Data handling

Do not commit credentials or unreviewed bulk datasets. Keep raw extracts local or in approved storage until licensing, privacy, retention, and repository-size considerations have been reviewed. Use small, properly attributed examples when public samples are needed.
