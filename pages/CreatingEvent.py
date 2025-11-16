import streamlit as st

name = st.text_input("Name: ", placeholder = "Type here...")

description = st.text_input("Description: ", placeholder= "Type here...")

locations = ["GMCS", "Billy Joel"]

norm_locs = {loc.strip().lower() for loc in locations}
desc_norm = description.strip().lower()

st.session_state.setdefault("created", False)
st.session_state.setdefault("created_name", "")
def create_event(who: str):
        st.session_state.created = True
        st.session_state.created_name = who.strip()

if description:
        if desc_norm in norm_locs:
            st.warning("A Similar Group Exists!")
            if st.button("Create"):
                  if name.strip():
                    create_event(name)
        else: 
            if st.button("Create!", use_container_width=True):
                if name.strip():
                    create_event(name)
                else:
                    st.warning("Please enter your name first.")
                    
if st.session_state.created:
    st.success(f"Your Event Has Been Created!, {st.session_state.created_name}!")








