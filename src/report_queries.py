from config import config
import pandas as pd
import psycopg2
import sys

class Queries():

    def __init__(self):
        self.conn = self.connect_db()
        self.cursor = self.conn.cursor()

    def connect_db(self):
        """Connect to a database"""

        conn = None

        try:
            print("connect")
            conn = psycopg2.connect(**config())

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            sys.exit()
        else:
            return conn

    def close_connections(self):
        """Close the cursor and connection."""

        self.cursor.close()
        self.conn.close()


    def get_daily_report(self, start_date, end_date):
        """Get daily report between start_date and end_date
        Args:
            start_date, end_date, dates in format YYYY-MM-DD
        """
        try:
            query = f"""SELECT consultantName, customerName, starttime,
                       ROUND((EXTRACT(EPOCH FROM (endtime - starttime)) / 3600),2) AS shift_time, 
                       ROUND((EXTRACT(EPOCH FROM (lunchend - lunchstart)) / 3600),2) AS lunch_time, 
                      (ROUND((EXTRACT(EPOCH FROM (endtime - starttime)) / 3600),2) - ROUND((EXTRACT(EPOCH FROM (lunchend - lunchstart)) / 3600),2)) AS  working_hours 
                       FROM time_entries WHERE DATE(starttime) BETWEEN  %s AND %s;"""
            self.cursor.execute(query, (start_date, end_date))
            df = pd.DataFrame(self.cursor.fetchall())
            df.columns = [desc[0] for desc in self.cursor.description]
            return df

        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error querying table {error}")
