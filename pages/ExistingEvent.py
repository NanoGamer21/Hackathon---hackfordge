# pages/ExistingEvent.py
import streamlit as st
import random
import string

st.set_page_config(page_title="Existing Events", layout="wide")

# ---- Typography to match Search page ----
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

# ---- Time + demo helpers (now hourly) ----
def hour_slots(start: int = 8, end: int = 22):
    """Return ['8:00 AM–9:00 AM', ..., up to end)."""
    def fmt(h):
        suf = "AM" if h < 12 else "PM"
        h12 = (h % 12) or 12
        return f"{h12}:00 {suf}"
    return [f"{fmt(h)}–{fmt(h+1)}" for h in range(start, end)]

BUILDINGS = ["ARTHN", "AH", "AL", "BT", "COMM", "E", "ENS", "FAC", "GMCS"]

def _rand_room():
    return f"{random.randint(100, 499)}{random.choice(string.ascii_uppercase)}"

def build_demo_events(topic: str, n: int = 3):
    times = random.sample(hour_slots(), k=min(n, len(hour_slots())))
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
            # NEW: include a description so cards can show it
            "description": f"A casual {topic} session. Come hang out and meet new people.",
        })
    return events

# ---- Get state ----
topic = st.session_state.get("choice") or "Featured"
events = st.session_state.get("events")
if not events:
    events = build_demo_events(topic, n=3)
    st.session_state.events = events

st.header(f"Events for: {topic}")

# Cards (now also show description when present)
labels = [
    f"{e['title']} — {e['time']} • {e['building']} {e['room']} • Host {e['host']} • {e['spots_left']} spots left"
    for e in events
]
for e in events:
    with st.container(border=True):
        st.subheader(e['title'])
        st.caption(f"{e['time']} • {e['building']} {e['room']} • Host {e['host']}")
        if e.get("description"):
            st.write(e["description"])
        st.progress(min(1.0, max(0.05, 1 - e['spots_left']/25)))
        st.write(f"Spots left: **{e['spots_left']}**")

st.divider()

# Select + actions
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
    if st.button("Reload", use_container_width=True):
        st.session_state.events = build_demo_events(topic, n=3)
        st.rerun()

st.page_link("pages/SearchP.py", label="← Back to search", icon="🔎")
