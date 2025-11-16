# pages/CreatingEvent.py
import streamlit as st
import random
import string

st.set_page_config(page_title="Create Event", layout="wide")

# ---- Typography to match Search/Existing pages ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Merriweather:wght@700;900&display=swap');
html, body, [data-testid="stAppViewContainer"]{
  font-family: "Inter", system-ui, -apple-system, Segoe UI, Roboto, sans-serif !important;
  -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;
}
h1, h2, h3, h4, h5, h6{
  font-family: "Merriweather", Georgia, "Times New Roman", serif !important;
  letter-spacing: .2px;
}
</style>
""", unsafe_allow_html=True)

# ---- Helpers ----
BUILDINGS = ["ARTHN", "AH", "AL", "BT", "COMM", "E", "ENS", "FAC", "GMCS"]
TIMES = ["8:00-8:30 AM", "8:30-9:00 AM", "9:00-9:30 AM", "9:30-10:00 AM", "10:00-10:30 AM",
         "10:30-11:00 AM", "11:00-11:30 AM", "11:30-12:00 PM", "12:00-12:30 PM", "12:30-1:00 PM",
         "1:00-1:30 PM", "1:30-2:00 PM", "2:00-2:30 PM", "2:30-3:00 PM", "3:00-3:30 PM",
         "3:30-4:00 PM", "4:00-4:30 PM", "4:30-5:00 PM", "5:00-5:30 PM", "5:30-6:00 PM",
         "6:00-6:30 PM", "6:30-7:00 PM", "7:00-7:30 PM", "7:30-8:00 PM", "8:00-8:30 PM",
         "8:30-9:00 PM", "9:00-9:30 PM", "9:30-10:00 PM"]

def _rand_room():
    return f"{random.randint(100, 499)}{random.choice(string.ascii_uppercase)}"

# ---- UI ----
st.markdown("<h1 style='margin:0'>Create an Event</h1>", unsafe_allow_html=True)
st.caption("Fill out the fields below to add a demo event.")

with st.container(border=True):
    user_name = st.text_input("Your Name:", placeholder="Type here...")
    event_name = st.text_input("Event Name:", placeholder="Type here...")
    description = st.text_input("Event Description:", placeholder="Type here...")
    selected_time = st.selectbox("Choose a time:", options=TIMES, index=None, placeholder="Select a time")

    cols = st.columns(2)
    with cols[0]:
        if st.button("Create!", type="primary", use_container_width=True):
            if not (user_name or "").strip():
                st.warning("Please enter your name.")
            elif not (event_name or "").strip():
                st.warning("Please enter your event name.")
            elif not (description or "").strip():
                st.warning("Please enter a description.")
            elif not selected_time:
                st.warning("Please select a time.")
            else:
                random_building = random.choice(BUILDINGS)
                # Build a demo event and push into session so it appears on ExistingEvent
                new_event = {
                    "id": f"evt_{random.randint(1000,9999)}",
                    "topic": st.session_state.get("choice") or event_name.strip(),
                    "title": event_name.strip(),
                    "time": selected_time,
                    "building": random_building,
                    "room": _rand_room(),
                    "host": user_name.strip(),
                    "spots_left": random.randint(5, 25),
                    "description": description.strip(),
                }
                events = st.session_state.get("events", [])
                events.insert(0, new_event)              # store new event first
                st.session_state.events = events
                st.session_state.choice = new_event["topic"]  # preselect this topic
                st.success(f"{user_name.strip()} created **{event_name.strip()}** at {random_building} at {selected_time}.")
                st.switch_page("pages/SearchP.py")       # go back to dropdown
    with cols[1]:
        st.page_link("pages/SearchP.py", label="Back to search", icon="🔎")
