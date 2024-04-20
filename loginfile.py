import streamlit as st
import pandas as pd

passwordlink = pd.read_csv('password.csv')

correctpass = passwordlink['password'].iloc[0]

st.dataframe(passwordlink)
st.write(correctpass)