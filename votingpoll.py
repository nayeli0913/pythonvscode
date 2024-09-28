#Create a voting poll for students
#Ask the name of voter
#Show each name of contestants and button to click or selectbox to vote for anyone
#Then save to CSV
#Show table
#Create downloadable csv file
#Plot chart of contestants (bar chart and pie chart) -make it switchable

import streamlit as st
import pandas as pd

csv = pd.read_csv('vote.csv')

name = st.text_input("Name of voter")
vote = st.selectbox("Choose who you want to vote for as prefect",['Lucas','Mike','Jane','Nancy','Will'])

if st.button("Submit vote"):
    dict = {'Name':[name],'Vote':[vote]}
    table = pd.DataFrame(dict)
    tablejoin = pd.concat([csv,table],ignore_index=True)
    tablejoin.to_csv('vote.csv',index=False)
    st.table(dict)
    st.success('vote submitted')