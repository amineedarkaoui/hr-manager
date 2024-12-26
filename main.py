import streamlit as st
from auth.auth import authenticate

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Login")
    with st.form("login_form"):
        email = st.text_input("email")
        password = st.text_input("password", type="password")
        if st.form_submit_button("login"):
            out, id = authenticate(email, password)
            if out is True:
                st.success("Login Successful")
                st.session_state.userId = id
                st.session_state.logged_in = True
            else:
                st.error(out)

if st.session_state.logged_in:
    st.title("Feedback Page")
    st.write("What do you think about the company's work environment?")
    answer1 = st.text_input("Your answer", key="answer1")

    st.write("What do you think about your salary?")
    answer2 = st.text_input("Your answer", key="answer2")

    st.write("What do you think about your managers?")
    answer3 = st.text_input("Your answer", key="answer3")

    if st.button("Submit"):
        st.write("answer1:", answer1, "answer2:", answer2, "answer3:", answer3)
else:
    login()
# # Initialize the page state in Session State
# if "current_page" not in st.session_state:
#     st.session_state.current_page = "login"  # Default page

# # Navigation Function
# def navigate_to(page_name):
#     st.session_state.current_page = page_name

# # Navigation Logic
# if st.session_state.current_page == "login":
#     login_page(navigate_to)
# elif st.session_state.current_page == "feedback":
#     feedback_page(navigate_to)