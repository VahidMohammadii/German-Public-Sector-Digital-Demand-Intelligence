# Code

This directory contains the planned implementation modules for the TED analytics workflow. Modules are separated by responsibility so source retrieval, quality controls, transformations, storage, analysis, and orchestration can be reviewed independently.

## Planned execution order

1. Ingestion retrieves source records and run metadata.
2. Data quality validates structure, identifiers, and completeness.
3. Transformations normalize and classify records.
4. Database loading stores records in the analytical model.
5. Analytics produces documented SQL metrics.
6. Orchestration runs configured steps and records outcomes.

At this initial stage, the folders contain module guidance and starter definitions. The TED API integration and end-to-end pipeline have not yet been implemented.
