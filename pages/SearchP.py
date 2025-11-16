# pages/SearchP.py
import streamlit as st
import random
import string

st.set_page_config(page_title="Search Events", layout="wide")

# Typography to match the rest of the app
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

# Demo/base data
BASE_TOPICS = ["Dungeons & Dragons", "CS Study Sesh", "LOCKIN IN ON EXAMS", "Math Club", "Clash Royale"]
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

def get_topics():
    topics = set(BASE_TOPICS)
    for e in st.session_state.get("events", []):
        if e.get("topic"):
            topics.add(e["topic"])
    return sorted(topics, key=str.casefold)

logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/San_Diego_State_Aztecs_logo.svg/2560px-San_Diego_State_Aztecs_logo.svg.png"

col_title, col_logo = st.columns([8, 1])
with col_title:
    st.markdown("<h1 style='margin:0'>Search Topics</h1>", unsafe_allow_html=True)
with col_logo:
    st.image(logo_url, width=120)

topics = get_topics()
default_idx = topics.index(st.session_state["choice"]) if st.session_state.get("choice") in topics else None

choice = st.selectbox(
    "Choose a topic (type to filter):",
    options=topics,
    index=default_idx,
    placeholder="Search"
)

if st.button("See Events", use_container_width=True):
    if choice:
        st.session_state.choice = choice
        # Only build fresh demo events if none exist yet for this topic
        if not st.session_state.get("events"):
            st.session_state.events = build_demo_events(choice, n=3)
        st.switch_page("pages/ExistingEvent.py")
    else:
        st.warning("Please select a topic from the dropdown.")

st.write("Don't see an event you like?")
if st.button("Create one!", use_container_width=True):
    st.switch_page("pages/CreatingEvent.py")
