# pages/CreatingEvent.py
import streamlit as st
import random
import string

st.set_page_config(page_title="Create Event", layout="wide")

# ---- Typography ----
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
def hour_slots(start: int = 8, end: int = 22):
    def fmt(h):
        suf = "AM" if h < 12 else "PM"
        h12 = (h % 12) or 12
        return f"{h12}:00 {suf}"
    return [f"{fmt(h)}–{fmt(h+1)}" for h in range(start, end)]

BUILDINGS = ["ARTHN", "AH", "AL", "BT", "COMM", "E", "ENS", "FAC", "GMCS"]

def _rand_room():
    return f"{random.randint(100, 499)}{random.choice(string.ascii_uppercase)}"

# ---- UI ----
st.markdown("<h1 style='margin:0'>Create an Event</h1>", unsafe_allow_html=True)
st.caption("Fill out the fields below to add a demo event.")

with st.container(border=True):
    user_name = st.text_input("Your Name:", placeholder="Type here...")
    event_name = st.text_input("Event Name:", placeholder="Type here...")
    description = st.text_input("Event Description:", placeholder="Type here...")
    selected_time = st.selectbox("Choose a time:", options=hour_slots(), index=None, placeholder="Select a time")

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
                new_event = {
                    "id": f"evt_{random.randint(1000,9999)}",
                    "topic": st.session_state.get("choice") or event_name.strip(),
                    "title": event_name.strip(),
                    "time": selected_time,                   # 1-hour block
                    "building": random_building,
                    "room": _rand_room(),
                    "host": user_name.strip(),
                    "spots_left": random.randint(5, 25),
                    "description": description.strip(),      # keep description
                }
                events = st.session_state.get("events", [])
                events.insert(0, new_event)
                st.session_state.events = events
                st.session_state.choice = new_event["topic"]  # preselect on return
                st.success(f"{user_name.strip()} created **{event_name.strip()}** at {random_building} at {selected_time}.")
                st.switch_page("pages/SearchP.py")
    with cols[1]:
        st.page_link("pages/SearchP.py", label="Back to search", icon="🔎")

