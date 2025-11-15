# SQL queries / functions

import psycopg2

def get_available_rooms(conn, building, requested_start, requested_end):
    cursor = conn.cursor()
    
    query = """
    SELECT *
    FROM rooms r
    WHERE r.building = %s
      AND r.id NOT IN (
        SELECT room_id
        FROM reservations
        WHERE start_time < %s
          AND end_time > %s
      )
    """
    
    cursor.execute(query, (building, requested_end, requested_start))
    return cursor.fetchall()