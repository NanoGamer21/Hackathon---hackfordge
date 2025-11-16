import streamlit as st

st.set_page_config(page_title="Search Events", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Merriweather:wght@700;900&display=swap');

/* Set body/UI font */
html, body, [data-testid="stAppViewContainer"]{
  font-family: "Inter", system-ui, -apple-system, Segoe UI, Roboto, sans-serif !important;
  -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;
}

/* Headings look more SDSU-like */
h1, h2, h3, h4, h5, h6{
  font-family: "Merriweather", Georgia, "Times New Roman", serif !important;
  letter-spacing: .2px;
}
</style>
""", unsafe_allow_html=True)

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

topic = choice 
st.write("Don't see an event you like?")
if st.button("Create one!", use_container_width=True,):
    st.switch_page("CreatingEvent.py")

