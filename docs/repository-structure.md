# Repository Structure

The repository will grow with the implementation. The tree below is a target structure; folders and components marked as planned may not exist yet.

```text
.
├── README.md
├── docs/
│   ├── architecture.md
│   ├── data-sources.md
│   ├── project-charter.md
│   └── repository-structure.md
├── code/
│   ├── ingestion/
│   │   ├── ted_api/
│   │   └── reference_data/
│   ├── data_quality/
│   ├── transformations/
│   ├── database/
│   │   ├── schema/
│   │   └── load/
│   ├── analytics/
│   │   ├── sql/
│   │   └── metrics/
│   └── orchestration/
├── powerbi/
│   └── screenshots/
└── data/
    └── .gitkeep
```

## Folder responsibilities

| Folder | Planned contents |
|---|---|
| `docs/` | Scope, architecture, source documentation, and implementation decisions |
| `code/ingestion/` | TED API client, query definitions, extraction jobs, and reference-data loaders |
| `code/data_quality/` | Schema, duplicate, completeness, and consistency checks |
| `code/transformations/` | Normalization, source linking, and digital-service classification |
| `code/database/` | SQL schema, views, and data-loading components |
| `code/analytics/` | SQL analyses and metric definitions |
| `code/orchestration/` | Pipeline entry point and safe example configuration |
| `powerbi/` | Power BI report deliverables and selected screenshots |
| `data/` | Local working data; raw or large extracts should generally remain untracked |

## Conventions

- Add folders when an implementation step needs them; Git does not track empty directories.
- Keep secrets in environment variables or a local ignored configuration file.
- Provide a sanitized example configuration such as `config.example.yaml`.
- Document derived categories and metrics close to their implementation.
- Avoid committing large raw datasets or files whose reuse terms have not been checked.
- Use clear commit and pull request descriptions that state what is implemented and what remains planned.
