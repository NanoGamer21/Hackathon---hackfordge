# Database connection & helper functions

import psycopg2

#connect with database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="LOL#numBER69",
    host="localhost",
    port=5432
)