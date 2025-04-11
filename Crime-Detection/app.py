import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
import time
import database as db
import update_database as ud


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:", layout="wide")

# --- DEMO PURPOSE ONLY --- #
placeholder = st.empty()
# placeholder.info("CREDENTIALS | username:pparker ; password:abc123")
# ------------------------- #

# --- USER AUTHENTICATION ---
users = db.fetch_all_users()

usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
passwords = [user["password"] for user in users]

credentials = {"usernames": {}}

for un, name, pw in zip(usernames, names, passwords):
    user_dict = {"name": name, "password": pw}
    credentials["usernames"].update({un: user_dict})


with st.container():
    if st.button('signup') == True:
        name = st.text_input("Name", placeholder='Enter your name')
        username = st.text_input("Username", placeholder='Enter username')
        password = st.text_input("password", placeholder='Enter the password')
        if st.button('submit'):
            ud.signup(name, username, password)

    else:

        name = st.text_input("Name", placeholder='Enter your name')
        username = st.text_input("Username", placeholder='Enter username')
        password = st.text_input("password", placeholder='Enter the password')
        authenticator = stauth.Authenticate(
            credentials, 'crime site', 'abcdefg')

        name, authentication_status, username = authenticator.login(
            "Login", "main")

        if authentication_status == False:
            st.error("Username/password is incorrect")

        if authentication_status == None:
            st.warning("Please enter your username and password")

        if authentication_status:
            placeholder.empty()

    # with st.sidebar:
    #     with st.echo():
    #         st.write("This code will be printed to the sidebar.")

    # with st.spinner("Loading..."):
    #     time.sleep(5)
    # st.success("Done!")

    # ---- HIDE STREAMLIT STYLE ----
    # hide_st_style = """
    #             <style>
    #             #MainMenu {visibility: hidden;}
    #             footer {visibility: hidden;}
    #             header {visibility: hidden;}
    #             </style>
    #             """
    # st.markdown(hide_st_style, unsafe_allow_html=False)
