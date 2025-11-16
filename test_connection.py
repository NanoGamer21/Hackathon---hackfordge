from db import get_db_connection

with get_db_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT now()")
        print("Connection successful, current time:", cur.fetchone()[0])
        