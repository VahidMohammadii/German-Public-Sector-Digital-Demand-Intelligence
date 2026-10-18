# TED API Ingestion

This module is intended to retrieve relevant published procurement notices and related award information from TED.

## Current status

This is a planning document. No API client or scheduled extraction job has been implemented yet.

## Planned responsibilities

- isolate TED API request and response handling;
- keep query definitions separate from transport logic;
- support documented pagination and bounded retries;
- record query scope, retrieval time, record counts, and run status;
- preserve source identifiers and provide traceability to retrieved records;
- report schema or request failures clearly.

## Planned layout

```text
ingestion/
├── ted_api/
│   ├── client.py
│   ├── queries.py
│   └── fetch_notices.py
└── reference_data/
    └── load_reference_data.py
```

The exact file names and implementation will be adjusted after the TED API operations and response schema are verified.

## Configuration and data safety

- Keep credentials and local environment-specific settings out of Git.
- Add a sanitized example configuration only after required settings are known.
- Do not commit raw bulk extracts before reviewing applicable reuse terms, privacy, and repository-size constraints.
- Log enough metadata to reproduce a query without exposing secrets.

See [the data source register](../../docs/data-sources.md) and [the planned architecture](../../docs/architecture.md).
