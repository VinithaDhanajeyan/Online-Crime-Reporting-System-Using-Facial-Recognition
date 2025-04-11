import streamlit as st
import time
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator

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

authenticator = stauth.Authenticate(
    credentials, 'crime site', 'abcdefg', cookie_expiry_days=30)

name, authentication_status, username = authenticator.login(
    "Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

# if authentication_status:
#     placeholder.empty()
