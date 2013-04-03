"""#
# This is a module that simulates memory for Hexy.
#"""

#imports
import sqlite3
from datetime import datetime, timedelta

class Memories(object):
    """Memories object."""
    def __init__(self, database = "memory"):
        self.file = database + ".sql"

    def open(self):
        #return a connection to the SQLite3 database file
        conn = sqlite3.connect(self.file)
        return conn, conn.cursor()

    def forget(self):
        #have Hexy start to forget things after a couple of weeks
        pass

class Interactions(Memories):
    """Memories about interaction times."""
    def __init__(self, database = "memory"):
        super(Interactions, self).__init__(database)

    def write(self, values):
        #write an interaction to Hexy's memory
        #expects values as a list of [start time, end time, type]
        conn, curs = self.open()
        values.insert(2, (values[1] - values[0]).total_seconds())       #insert time delta as a float to values
        curs.execute (
                        """INSERT INTO 
                        INTERACTIONS (
                            start_time,
                            stop_time,
                            duration,
                            type
                            )
                        VALUES (
                            ?, ?, ?, ?
                            )""", values
        )
        conn.commit()

    def getLast(self):
        #return the timedate stamp of the last interaction Hexy had with a user
        conn, curs = self.open()
        return curs.execute (
                            """SELECT MAX(stop_time)
                            from interactions"""
        ).fetchone()[0]

    def getWeekly(self):
        #return the number of seconds of interaction Hexy has had with a user for the past week
        conn, curs = self.open()
        week = (datetime.now() - timedelta(days=7),)
        return curs.execute (
                            """SELECT SUM(duration)
                            FROM interactions
                            WHERE stop_time > ?""", week
        ).fetchone()[0]
        