import streamlit as st

# Page configuration
st.set_page_config(page_title="Search a Subject", page_icon="🔎", layout="centered")

# Require login
if "user" not in st.session_state:
    st.error("Please sign in with your @sdsu.edu account to continue.")
    st.stop()

# Header
st.markdown(
    """
    <div style="display:flex; flex-direction:column; align-items:center; margin-top:20px;">
        <h1 style="margin:0; font-family:sans-serif;">Search a Subject</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Topics list
topics = [
    "Dungeons & Dragons",
    "CS Study Sesh",
    "LOCKIN IN ON EXAMS",
    "Math Club",
    "Clash Royale"
]
topics = sorted(topics, key=str.casefold)

# Dropdown
choice = st.selectbox(
    "Choose a topic (type to filter):",
    options=topics,
    index=None,
    placeholder="Search"
)

# Create button
if st.button("Create an Event!", use_container_width=True):
    st.write(f"Event created for: {choice}")


