import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')


correctpass = "nayeli123"

pass1, pass2 = st.sidebar.columns([1,2])

with pass1:
    password = st.sidebar.text_input("Please enter password",type='password')

login = st.sidebar.button("Login")

if login:
    if password:
        if password == correctpass:
            csvlink = pd.read_csv('employee.csv')
            st.dataframe(csvlink)
        else:
            st.sidebar.error("Password incorrect")
    else:
        st.sidebar.error("Please enter a password")