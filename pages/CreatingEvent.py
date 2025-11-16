import streamlit as st
import random

user_name = st.text_input("Your Name: ", placeholder = "Type here...")

event_name = st.text_input("Event Name: ", placeholder = "Type here...")

description = st.text_input("Event Description: ", placeholder= "Type here...")

times = ["8:00-8:30 AM", "8:30-9:00 AM", "9:00-9:30 AM", "9:30-10:00 AM", "10:00-10:30 AM", "10:30-11:00 AM", "11:00-11:30 AM", 
         "11:30-12:00 PM", "12:00-12:30 PM", "12:30-1:00 PM", "1:00-1:30 PM", "1:30-2:00 PM", "2:00-2:30 PM", "2:30-3:00 PM",
         "3:00-3:30 PM", "3:30-4:00 PM", "4:00-4:30 PM", "4:30-5:00 PM", "5:00-5:30 PM", "5:30-6:00 PM", "6:00-6:30 PM", "6:30-7:00 PM",
         "7:00-7:30 PM", "7:30-8:00 PM", "8:00-8:30 PM", "8:30-9:00 PM", "9:00-9:30 PM", "9:30-10:00 PM"]

buildings = ["ARTHN", "AH", "AL", "BT", "COMM", "E", "ENS", "FAC", "GMCS"]

selected_time = st.selectbox("Choose a time:", options=times, index=None, placeholder="Select a time")

if st.button("Create!"):
    if not user_name.strip():
        st.warning("Please enter your name.")
    elif not event_name.strip():
        st.warning("Please enter your event name.")
    elif not description.strip():
        st.warning("Please enter a description.")
    elif not selected_time:
        st.warning("Please select a time.")
    else:
        random_building = random.choice(buildings)
        when = st.success(f"{user_name.strip()} has created an event at {random_building} at {selected_time}. Have fun at: {event_name.strip()}")
