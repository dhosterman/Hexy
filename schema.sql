CREATE TABLE IF NOT EXISTS
INTERACTIONS (
    id INTEGER PRIMARY KEY,
    start_time TIMESTAMP,
    stop_time TIMESTAMP,
    duration REAL,
    type INT
    );

CREATE TABLE IF NOT EXISTS
INTERACTION_TYPES (
    id INTEGER PRIMARY KEY,
    interaction_id INTEGER,
    description TEXT
    );

INSERT INTO INTERACTION_TYPES (
    interaction_id,
    description
    )
VALUES (1, "General Interaction");
