import streamlit as st
import random

st.set_page_config(page_title="existingEvent")

choice = st.session_state.get("choice", None)

st.header(f"Event: {choice}")

times = ["8:00-8:30 AM", "8:30-9:00 AM", "9:00-9:30 AM", "9:30-10:00 AM", "10:00-10:30 AM", "10:30-11:00 AM", "11:00-11:30 AM"]
buildings = ["ARTHN", "AH", "AL", "BT", "COMM", "E", "ENS", "FAC", "GMCS"]

random_building = random.choice(buildings)
random_time = random.choice(times)


location = st.selectbox(
    "Location: ",
    options = buildings,
    index = None,
    placeholder = "Select..."
)

#Selecting a time
st.subheader(f"Location: {random_building}")
st.subheader(f"Time: {random_time}")

if st.button("Join Event"):
    st.success(f"You have joined the event '{choice}' at {random_building} at {random_time}. Enjoy!")









