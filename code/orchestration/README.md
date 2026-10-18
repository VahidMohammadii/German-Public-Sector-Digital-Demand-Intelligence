# Orchestration

Planned responsibility: run ingestion, validation, transformation, loading, and post-load checks in a documented order.

The runner should return a non-zero status when a required stage fails, write a run record, and avoid refreshing downstream reports after a failed load. Configuration should support local execution first; hosted scheduling is a later deployment decision.

No scheduler or end-to-end pipeline is implemented yet.
