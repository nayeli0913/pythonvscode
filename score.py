import streamlit as st

st.title("Math scoresheet app")

st.subheader("input your math grade to find out your score")

grade = st.number_input("Enter your math grade",0,100,value=100)
if st.button("check grade"):
  if (grade >= 90):
    st.success("A+")
  elif(grade >= 80):
    st.success("A")
  elif(grade >= 70):
    st.success("B")
  elif(grade >= 60):
    st.warning("C")
  elif(grade >= 50):
    st.warning("D")
  elif(grade < 50):
    st.error("F")