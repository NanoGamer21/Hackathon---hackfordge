import streamlit as st

name = st.text_input("Name: ", placeholder = "Type here...")

description = st.text_input("Description: ", placeholder= "Type here...")

locations = ["GMCS", "Billy Joel"]

norm_locs = {loc.strip().lower() for loc in locations}
desc_norm = description.strip().lower()

if description:
        if desc_norm in norm_locs:
            st.write("A Similar Group Exists!")
            st.write("Do you still wanna create?")
            choice = st.button (
                "Create"
            )
        else: 
            if st.button("Create!", use_container_width=True):
                 st.write("Hello!")








