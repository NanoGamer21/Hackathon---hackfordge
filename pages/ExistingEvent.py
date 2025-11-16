# pages/ExistingEvent.py
import streamlit as st
import random
import string

st.set_page_config(page_title="Existing Events", layout="wide")

# Fallback demo builder if page is opened directly
TIMES = ["8:00–8:30 AM", "8:30–9:00 AM", "9:00–9:30 AM", "9:30–10:00 AM",
         "10:00–10:30 AM", "10:30–11:00 AM", "11:00–11:30 AM", "11:30–12:00 PM"]
BUILDINGS = ["ARTHN", "AH", "AL", "BT", "COMM", "E", "ENS", "FAC", "GMCS"]

def _rand_room():
    return f"{random.randint(100, 499)}{random.choice(string.ascii_uppercase)}"

def build_demo_events(topic: str, n: int = 3):
    times = random.sample(TIMES, k=min(n, len(TIMES)))
    buildings = random.sample(BUILDINGS, k=min(n, len(BUILDINGS)))
    events = []
    for i in range(len(times)):
        events.append({
            "id": f"evt_{random.randint(1000,9999)}",
            "topic": topic,
            "title": f"{topic} Meetup",
            "time": times[i],
            "building": buildings[i],
            "room": _rand_room(),
            "host": random.choice(["Alex", "Jordan", "Taylor", "Sam", "Riley"]),
            "spots_left": random.randint(3, 20),
        })
    return events

topic = st.session_state.get("choice")
events = st.session_state.get("events")

if not topic:
    topic = "Featured"
if not events:
    events = build_demo_events(topic, n=3)
    st.session_state.events = events

st.header(f"Events for: {topic}")

# Show the three demo events as cards + a selector
labels = [
    f"{e['title']} — {e['time']} • {e['building']} {e['room']} • Host {e['host']} • {e['spots_left']} spots left"
    for e in events
]

# Pretty cards
for e in events:
    with st.container(border=True):
        st.subheader(f"{e['title']}")
        st.caption(f"{e['time']} • {e['building']} {e['room']} • Host {e['host']}")
        st.progress(min(1.0, max(0.05, 1 - e['spots_left']/25)))  # playful fill
        st.write(f"Spots left: **{e['spots_left']}**")

st.divider()

# Selection + join
idx_options = list(range(len(events)))
selected_idx = st.selectbox(
    "Pick an event to join:",
    options=idx_options,
    format_func=lambda i: labels[i],
    index=None,
    placeholder="Select an event..."
)

col1, col2 = st.columns([1,1])
with col1:
    if st.button("Join Event", type="primary", use_container_width=True):
        if selected_idx is None:
            st.warning("Please select an event first.")
        else:
            sel = events[selected_idx]
            st.session_state.joined_event = sel
            st.success(f"You joined '{sel['title']}' at {sel['building']} {sel['room']} at {sel['time']}. Enjoy!")
with col2:
    if st.button("Shuffle suggestions", use_container_width=True):
        st.session_state.events = build_demo_events(topic, n=3)
        st.rerun()

st.page_link("pages/SearchP.py", label="← Back to search", icon="↩️")
