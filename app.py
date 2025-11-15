import streamlit as st

st.title("Hello Streamlit!")
st.write("This is my first web app.")
number = st.slider("Pick a number", 1, 100)
st.write("You picked:", number)
