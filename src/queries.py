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

    def print_all_rows(self, table: str):
        """Print all the rows.

        Args:
            table, name of the table
        """

        if table not in ["time_entries"]:
            print("Not a valid table.")
            return 1

        try:
            query = f"""SELECT * FROM {table};"""
            self.cursor.execute(query)
            df = pd.DataFrame(self.cursor.fetchall()) 

            column_names = [desc[0] for desc in self.cursor.description]
            df.columns = column_names
            print(df)

        except ( Exception, psycopg2.DatabaseError) as error:
            print(f"Error querying table {table} {error}")
            self.close_connections()


