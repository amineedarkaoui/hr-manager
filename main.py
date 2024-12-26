import streamlit as st
from auth.auth import authenticate
from DB.database import store_feedback
from Modele.sentiment_analysis_model import modele
from reports.email import send_feedback_email
from dashboard.dashboard import salary_by_departement,feedback_pie_chart

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

def login():
    st.title("Login")
    with st.form("login_form"):
        email = st.text_input("email")
        password = st.text_input("password", type="password")
        if st.form_submit_button("login"):
            out, user = authenticate(email, password)
            if out is True:
                st.success("Login Successful")
                st.session_state.user = user
                st.session_state.logged_in = True
            else:
                st.error(out)

    st.write("or")
    if st.button("Go to dashboard"):
        st.session_state.page = "dashboard"

def feedback_page():
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
    st.title("Feedback Page")
    answer1 = st.text_input("What do you think about the company's work environment?", key="answer1")
    answer2 = st.text_input("What do you think about your salary?", key="answer2")
    answer3 = st.text_input("What do you think about your managers?", key="answer3")
    if st.button("Submit"):
        sentiment1, sentiment2, sentiment3 = modele(answer1)[0]['label'], modele(answer2)[0]['label'], modele(answer3)[0]['label']
        store_feedback(st.session_state.user[0], answer1, answer2, answer3, sentiment1, sentiment2, sentiment3)
        send_feedback_email(st.session_state.user, answer1, answer2, answer3, sentiment1, sentiment2, sentiment3)
        st.success("Feedback submitted successfully")

    if st.button("Go to dashboard"):
        st.session_state.page = "dashboard"

def dashboard_page():
    st.title("Data visualization")
    feedback_pie_chart()
    salary_by_departement()
    if st.button("Go back to login"):
        st.session_state.logged_in = False
        st.session_state.page = "login"

if st.session_state.page == "dashboard":
    dashboard_page()
elif st.session_state.logged_in:
    feedback_page()
else:
    login()