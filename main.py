import streamlit as st

# pg = st.navigation([
#         st.Page("Pages/login_page.py", url_path="login"),
#         st.Page("Pages/feedback_page.py", url_path="feedback"),
#     ],
#     position='hidden'
# )
# pg.run()

# Initialize the page state in Session State
if "current_page" not in st.session_state:
    st.session_state.current_page = "login"  # Default page

# Navigation Function
def navigate_to(page_name):
    st.session_state.current_page = page_name

# Navigation Logic
if st.session_state.current_page == "login":
    login_page(navigate_to)
elif st.session_state.current_page == "feedback":
    feedback_page(navigate_to)