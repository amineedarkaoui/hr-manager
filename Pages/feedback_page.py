import streamlit as st

def feedback_page(navigate_to):
    st.title("Feedback Page")
    with st.form("login_form"):
        st.write("What do you think about the company's work environment?")
        answer1 = st.text_input("Your answer")
        st.write("What do you think about your salary?")
        answer2 = st.text_input("Your answer")
        st.write("What do you think about your managers?")
        answer3 = st.text_input("Your answer")
    