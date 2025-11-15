# streamlit frontend + backend logic

import streamlit as st

# TESTING
st.title("Testing")

st.write("""
Hello World!
""")

# general structure of app
'''
campus_app/
├─ app.py            # Streamlit frontend + main logic
├─ db.py             # Database connection & helper functions
├─ queries.py        # SQL queries / functions
├─ requirements.txt
'''

### BACKEND LOGIC - INTERACTING WITH THE DATABASE ###

# Objects/databases: Classrooms, Reservations, Users
'''
    * Maybe there are separate tables for each type of user as well (admin, faculty, students)
    * 
'''

# checking availability
'''
Variables we need to check
    * Class (ClassID and Location)
        => ClassID: int (ex: 9932 - not sure if we have a class)
        => Location: String (ex: "GMCS 405")
        => Do classrooms have separate room ID's?
        => If not, we will probably 
    * Current Time
        => Python does have datetime datatypes
        => So we can either use datetime, or alternate between int and string
            => PostgreSQL also has robust DATE and TIME data types
    * We can obtain the actual classroom from the classroom database
    * 

Logic
    * Obtain the classroom from the classroom database (unique id for it)
    * Check all the reservations for that classroom
    * If there is any reservation where start_time < requested_end AND end_time > requested_start, set boolean (availability) to false
    * Otherwise, set boolean to true

Variables

Functions
    * get_class() => use embedded SQL query
    * get_reservation() => use embedded SQL query
    * def get_current_time() => return datetime.now()
    * 
'''

# SUP BOIZ