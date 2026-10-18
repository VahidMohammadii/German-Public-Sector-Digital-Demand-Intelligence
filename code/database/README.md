# Database

Planned responsibility: define and load the SQL analytical store.

The first model should keep notices and awards distinguishable, preserve source identifiers, and retain run provenance. The exact schema will be finalized after inspecting actual TED response fields.

- `schema/`: table and view definitions
- `load/`: validated data-loading logic

No database connection or load process is implemented yet. Keep credentials in environment variables or ignored local configuration.
