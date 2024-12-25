import streamlit as st

st.title("Login Page")
with st.form("login_form"):
    email = st.text_input("email")
    password = st.text_input("password", type="password")
    if st.form_submit_button("login"):
