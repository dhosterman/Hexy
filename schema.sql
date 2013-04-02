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

CREATE TABLE IF NOT EXISTS
INPUTS (
    id INTEGER PRIMARY KEY,
    input BLOB,
    clarification TEXT,
    output_id INTEGER
    );

CREATE TABLE IF NOT EXISTS
OUTPUTS (
    id INTEGER PRIMARY KEY,
    mood INTEGER,
    action INTEGER,
    output TEXT
    );

INSERT INTO INPUTS (
    id,
    input,
    clarification,
    output_id
    )
VALUES (1, "['goodbye', 'sayonara']", "Are you going away for a while?", 1),
    (2, "['goodbye']", "Should I go to sleep now?", 1);

INSERT INTO OUTPUTS (
    id,
    mood,
    action,
    output)
VALUES (1, 1, 1, "['Goodbye!', 'See you later!', 'Goodnight!']");
