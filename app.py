import streamlit as st

st.set_page_config(page_title="My App", page_icon="🔑")

# simple session flag
if "authed" not in st.session_state:
    st.session_state.authed = False

if not st.session_state.authed:
    st.title("Sign in")
    with st.form("login"):
        pw = st.text_input("Passcode", type="password")
        go = st.form_submit_button("Enter")
    if go:
        if pw == st.secrets.get("APP_PASSCODE"):
            st.session_state.authed = True
            st.success("Signed in!")
            st.rerun()
        else:
            st.error("Invalid passcode.")
    st.stop()

# ---- protected content below ----
st.sidebar.button("Log out", on_click=lambda: (st.session_state.update(authed=False), st.rerun()))
st.title("Welcome 👋")
st.write("Your Streamlit application begins here!")
