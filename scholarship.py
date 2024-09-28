#Write a Python program for students to check their scholarship eligibility. Create a menu for the "Check Scholarship" page and the "Scholarship Database" page.


#Ask for the student's name.
#Ask for their GPA.
#Based on their GPA, determine what type of scholarship they are eligible for:
#If their GPA is below 2.5, they are not eligible for a scholarship.
#If their GPA is between 2.5-3.0, they are eligible for a partial scholarship.
#If their GPA is between 3.0-3.5, they are eligible for a half scholarship.
#If their GPA is between 3.5-4.0, they are eligible for a full scholarship.
#Implement the program so that it displays the appropriate message to the student based on their GPA.

import streamlit as st

name = st.text_input("Enter your name")
gpa = st.number_input("Enter your GPA")

if st.button("Submit"):
  if gpa < 2.5:
    st.write("Sorry, you are not eligible for a scholarship.")
  elif gpa < 3.0:
    st.write("You are eligible for a partial scholarship.")
  elif gpa < 3.5:
    st.write("You are eligible for a half scholarship.")
  else:
    st.write("Congratulations, you are eligible for a full scholarship!")