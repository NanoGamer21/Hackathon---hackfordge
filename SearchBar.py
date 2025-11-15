import streamlit as st

st.set_page_config(page_title="Demo", layout="centered")

# Your existing topics for the dropdown
topics = ["Dungeons & Dragons", "CS Study Sesh", "LOCKIN IN ON EXAMS", "Math Club", "Clash Royale"]
topics = sorted(topics, key=str.casefold)
st.title("Search a Subject")

# A. Dropdown that filters as you type
choice = st.selectbox(
    "Choose a topic (type to filter):",
    options=topics,
    index=None,                               # so nothing is preselected
    placeholder="Search"
)

topic = choice 

if st.button("Creat an Event!", use_container_width=True):
    st.write("Hello!")

