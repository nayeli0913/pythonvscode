import streamlit as st

st.title("Here is a calculator app")

st.header("Welcome")

st.subheader("This is a python app")

name = st.text_input("Enter your name")

yob = st.number_input("Enter your year of birth",1950,2023,value= 1950)

curr = st.number_input("Enter your current year",2023,value= 2023)

age = curr - yob

if st.button("Check Age"):

    st.write(f"{name} you will be {age} in year {curr}")

    st.success(f"{name} you will be {age} in year {curr}")