# Database connection & helper functions

import psycopg2

# import database_2 as db_2

# connect with database

conn_string = 'postgresql://neondb_owner:npg_Iblu3NTXBWq6@ep-rapid-bread-a4y7kred-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
# conn = psycopg2.connect(conn_string)

def get_connection():
    try:
        conn = psycopg2.connect(conn_string)
        # print("Connected to database sucessfully!")
        return conn

    except Exception as e:
        print("Connection failed:", e)

# obtain a list of all rooms
def fetch_all_rooms():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM room")
    rows = cursor.fetchall()
    conn.close()
    return rows

# obtain a list of all resevations
def fetch_all_reservations():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return rows

