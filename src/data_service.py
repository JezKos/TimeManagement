import psycopg2
from psycopg2.extras import RealDictCursor
from config import config
import json


            
def db_create_entry(consultantName, customerName, startTime, endTime, lunchStart, lunchEnd):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'INSERT INTO time_entries (consultantName, customerName, startTime, endTime, lunchStart, lunchEnd) VALUES (%s, %s, %s, %s, %s, %s);'
        cursor.execute(SQL, (consultantName, customerName, startTime, endTime, lunchStart, lunchEnd))
        con.commit()
        result = {"success": "created entry name: %s " % consultantName}
        cursor.close()
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

if __name__ == "__main__":
    db_create_entry("Sanna Reponen", "Skillio", "2025-10-20 09:00:00", "2025-10-20 17:00:00", "2025-10-20 12:00:00", "2025-10-20 13:00:00")