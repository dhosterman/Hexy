"""#
# Module to initialize Sqlite Database.
#"""

#imports
import sqlite3

#global variables
database = "memory.sql"

def initInputs(conn, curs):
    #initialize the inputs table and insert default values
    inputs = (
        (1, "['goodbye', 'sayonara']", 'Are you going away for a while?', 1),
        (2, "['goodbye']", 'Should I go to sleep now?', 1)
        )
    
    curs.execute (
        """CREATE TABLE IF NOT EXISTS
        inputs (
            id INTEGER PRIMARY KEY,
            input BLOB,
            clarification TEXT,
            output_id INTEGER
            )"""
        )

    curs.executemany (
        """REPLACE INTO inputs VALUES (
            ?, ?, ?, ?
            )""", inputs
        )

    conn.commit()

def initOutputs(conn, curs):
    #initialize the outputs table and insert default values
    outputs = (
        (1, 1, 1, "['Goodbye!', 'See you later!', 'Goodnight!']"),
        )

    curs.execute (
        """CREATE TABLE IF NOT EXISTS
        outputs (
            id INTEGER PRIMARY KEY,
            mood INTEGER,
            action INTEGER,
            output TEXT
            )"""
        )

    curs.executemany (
        """REPLACE INTO outputs VALUES (
            ?, ?, ?, ?
            )""", outputs
        )

    conn.commit()

def initInteractions(conn, curs):
    #initialize the interactions table

    curs.execute (
        """CREATE TABLE IF NOT EXISTS
        interactions (
            id INTEGER PRIMARY KEY,
            start_time TIMESTAMP,
            stop_time TIMESTAMP,
            duration REAL,
            type INTEGER
            )"""
        )

    conn.commit()

def initInteractionTypes(conn, curs):
    #initialize the interaction_types table and insert default values
    interactions = (
        (1, 1, 'General Interaction'),
        )

    curs.execute(
        """CREATE TABLE IF NOT EXISTS
        interaction_types (
            id INTEGER PRIMARY KEY,
            interaction_id INTEGER,
            description TEXT
            )"""
        )

    curs.executemany (
        """REPLACE INTO interaction_types VALUES (
            ?, ?, ?
            )""", interactions
        )

    conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    initInputs(conn, curs)
    initOutputs(conn, curs)
    initInteractions(conn, curs)
    initInteractionTypes(conn, curs)