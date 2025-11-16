import streamlit as st

# Minimal launcher: keep app entrypoint at repo root and redirect to the Login page in `pages/`.
st.set_page_config(page_title="Room Reserve", page_icon="🎓")

# Redirect straight to the Login page (keeps root `app.py` as the entrypoint Streamlit expects).
st.switch_page("Login")