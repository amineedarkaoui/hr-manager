import streamlit as st
from auth.auth import authenticate

st.title("Login Page")
with st.form("login_form"):
    email = st.text_input("email")
    password = st.text_input("password", type="password")
    if st.form_submit_button("login"):
        out = authenticate(email, password)
        if out == True:
            st.success("Login Successful")
            st.switch_page("Pages/feedback_page.py")
        else:
            st.error(out)