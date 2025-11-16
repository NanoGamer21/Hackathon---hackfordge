import streamlit as st

st.set_page_config(page_title="Search Events", layout="wide")


# Existing topics for the dropdown
topics = ["Dungeons & Dragons", "CS Study Sesh", "LOCKIN IN ON EXAMS", "Math Club", "Clash Royale"]
topics = sorted(topics, key=str.casefold)

logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/San_Diego_State_Aztecs_logo.svg/2560px-San_Diego_State_Aztecs_logo.svg.png"

col_title, col_logo = st.columns([8, 1])
with col_title:
    st.markdown("<h1 style='margin:0'>Search a Subject</h1>", unsafe_allow_html=True)
with col_logo:
    st.image(logo_url, width=120)

# Dropdown that filters as you type
choice = st.selectbox(
    "Choose a topic (type to filter):",
    options=topics,
    index = None,   #Nothing is preselected
    placeholder="Search"
)

if st.button("Go to Event"):
    if choice:
        st.session_state.choice = choice
        st.experimental_set_query_params(page="ExistingEvent.py")
        st.switch_page("pages/ExistingEvent.py")
    else:
        st.warning("Please select a topic from the dropdown.")
