# Database loading

Planned responsibility: load validated and standardized records into the SQL model using stable identifiers and safe repeatable operations.

Loading should be idempotent where practical, preserve run provenance, and distinguish inserts from updates. Failed or partial runs must be visible and should not be reported as a successful refresh.

No loader or database credentials are included yet.
