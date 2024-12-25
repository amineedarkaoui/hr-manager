import streamlit as st

pg = st.navigation([st.Page("Pages/login_page.py", url_path="login")], position='hidden')
pg.run()