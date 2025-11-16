# SQL queries / functions

import sys
import psycopg2
import database as db

def get_available_rooms(building, requested_start, requested_end):
    conn = db.get_connection()
    cursor = conn.cursor()

    # check if requested time range is valid
    if requested_start >= requested_end:
      sys.exit("Please pick a valid time range")
    
    # select any room in building that do NOT have reservations
    # overlapping with requested reservation time-range
    query = """
    SELECT *
    FROM room r
    WHERE r.room_building = %s
      AND r.room_id NOT IN (
        SELECT room_id
        FROM reservations
        WHERE reservation_start::time < %s
          AND reservation_end::time > %s
      )
    """
    
    cursor.execute(query, (building, requested_end, requested_start))
    results = cursor.fetchall()
    cursor.close()
    return results