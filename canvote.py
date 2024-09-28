import streamlit as st
import pandas as pd

csv = pd.read_csv('canvote.csv')

st.image('https://www.ramara.ca/en/municipal-office/resources/Documents/Elections/2024-By-Election/Voters.jpg')
name = st.text_input("Name")
age = st.number_input("Enter your age")

if age < 18:
    st.subheader(f"Sorry {name}, you are not eligible to vote")
else:
    vote = st.radio("Who would you like to vote for?",['Donald trump','Kamala Harris'],horizontal=True)
    if st.button("Enter"):
        dict = {'Name':[name],'Vote':[vote]}
        table = pd.DataFrame(dict)
        tablejoin = pd.concat([csv,table],ignore_index=True)
        tablejoin.to_csv('canvote.csv',index=False)
        st.table(dict)
        if vote == 'Donald trump':
            st.success(f"{name}, you have voted for Donald trump")
        else:
            st.success(f"{name}, you have voted for Kamala Harris")