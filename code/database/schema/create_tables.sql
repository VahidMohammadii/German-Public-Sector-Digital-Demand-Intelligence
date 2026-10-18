-- Starter schema for the project foundation.
-- Validate field names, lengths, and relationships against actual TED API payloads
-- before using this as a production schema.

CREATE TABLE IF NOT EXISTS ingestion_runs (
    run_id              INTEGER PRIMARY KEY,
    source_name         VARCHAR(100) NOT NULL,
    query_scope         TEXT NOT NULL,
    started_at_utc      TIMESTAMP NOT NULL,
    finished_at_utc     TIMESTAMP,
    status              VARCHAR(30) NOT NULL,
    records_received    INTEGER,
    records_processed   INTEGER,
    error_summary       TEXT
);

CREATE TABLE IF NOT EXISTS notices (
    notice_id           VARCHAR(200) PRIMARY KEY,
    notice_type         VARCHAR(100),
    publication_date    DATE,
    deadline_date       DATE,
    buyer_identifier    VARCHAR(200),
    buyer_name          TEXT,
    country_code        CHAR(2),
    nuts_code           VARCHAR(20),
    cpv_code            VARCHAR(20),
    title               TEXT,
    procurement_status  VARCHAR(100),
    source_url          TEXT,
    first_seen_run_id   INTEGER REFERENCES ingestion_runs(run_id),
    last_seen_run_id    INTEGER REFERENCES ingestion_runs(run_id)
);

CREATE TABLE IF NOT EXISTS awards (
    award_id            VARCHAR(200) PRIMARY KEY,
    notice_id           VARCHAR(200) REFERENCES notices(notice_id),
    award_date          DATE,
    reported_value      NUMERIC(20, 4),
    currency_code       CHAR(3),
    supplier_identifier VARCHAR(200),
    supplier_name       TEXT,
    source_url          TEXT,
    first_seen_run_id   INTEGER REFERENCES ingestion_runs(run_id),
    last_seen_run_id    INTEGER REFERENCES ingestion_runs(run_id)
);

CREATE INDEX IF NOT EXISTS idx_notices_publication_date
    ON notices(publication_date);

CREATE INDEX IF NOT EXISTS idx_notices_cpv_code
    ON notices(cpv_code);

CREATE INDEX IF NOT EXISTS idx_notices_buyer_identifier
    ON notices(buyer_identifier);

CREATE INDEX IF NOT EXISTS idx_awards_notice_id
    ON awards(notice_id);
