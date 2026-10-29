# Code

This directory is the planned home for modular implementation components: source ingestion, data-quality checks, transformations, database loading, analytics, and orchestration.

As of 2026-10-29, an end-to-end TED ingestion script (`ted_ingest_v3.py`) has been tested locally with MySQL. The script is still in the owner's Downloads folder and has not yet been committed here. These folders therefore remain implementation targets; the local proof of concept is documented in [Implementation Status](../docs/implementation-status.md).

## Planned modularization

1. Ingestion retrieves source records and run metadata.
2. Data quality validates structure, identifiers, and completeness.
3. Transformations normalize and classify records.
4. Database loading stores records in the analytical model.
5. Analytics produces documented SQL metrics.
6. Orchestration runs configured steps and records outcomes.
