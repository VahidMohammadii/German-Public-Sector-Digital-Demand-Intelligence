# Data Source Register

## Primary source: Tenders Electronic Daily (TED)

| Field | Current / planned value |
|---|---|
| Source | Tenders Electronic Daily (TED), the EU public procurement notices service |
| Access | TED public API, `POST /v3/notices/search` |
| Current query scope | Buyers in Germany; publication dates 2016-10-28 through 2026-10-29 inclusive |
| Current query | `buyer-country=DEU AND publication-date>=20161028 AND publication-date<20261030` |
| Intended records | Published notices; related award information may be considered in a later stage |
| Query validation | Completed; TED reported 1,316,938 matches |
| Retrieval status | In progress locally; 122,500 records processed across 490 pages at the last observed checkpoint |
| Pagination | Iteration-token mode; 250 notices per observed page |
| Documentation | [TED Developer Portal](https://docs.ted.europa.eu/) · [TED API documentation](https://docs.ted.europa.eu/api/latest/index.html) |

The matching count is not the number already stored in MySQL. See [Implementation Status](implementation-status.md) for run progress and the checkpoint interruption.

## Selected fields

The initial field set includes notice publication number and date, notice type, title, buyer name and country, CPV classification, and tender deadline. The actual response mapping must be checked against the local script and representative records before it is documented as final.

## Reference data

The local setup includes 9,454 CPV reference descriptions retrieved from TED reference material. Record the source version and retrieval details when the reference data is packaged for reproducible use.

## Coverage and interpretation limits

- TED contains published notices available through the service, not every purchase made by every German public body.
- Analysis depends on the selected query, date range, notice types, and fields returned.
- Award notices may be missing, delayed, or not linkable to an original notice.
- Buyer, supplier, CPV, and geography fields can be incomplete or inconsistent.
- Notice counts are not equivalent to total addressable market, revenue, or realized expenditure.
- Historical patterns do not establish future demand, profitability, or bid success.

## Data handling

Do not commit credentials, checkpoint files, continuation tokens, or unreviewed bulk datasets. Keep raw extracts local or in approved storage until licensing, privacy, retention, and repository-size considerations have been reviewed.
