#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -save and update in a csv file

import streamlit as st

import pandas as pd

st.set_page_config(layout='wide')

#csv file is a text file where each data is seperated by a comma (comma seperated value)

df = pd.read_csv('scores.csv')
st.dataframe(df,use_container_width=True)

c1,c2 = st.columns(2)

with c1:
  name = st.text_input("Enter your name")

c3,c4 = st.columns(2)

with c3:
  mat = st.number_input("Enter your math score")

with c4:
  eng = st.number_input("Enter your english score")

c5,c6 = st.columns(2)

with c5:
  sci = st.number_input("Enter your science score")

with c6:
  tec = st.number_input("Enter your computer sci score")

average = (tec+sci+eng+mat)/4

if (average >= 90):
    grade ="A+"
elif(average >= 80):
    grade ="A"
elif(average >= 70):
    grade ="B"
elif(average >= 60):
    grade ="C"
elif(average >= 50):
    grade ="D"
elif(average < 50):
    grade ="F"

total = mat+sci+tec+eng

#this function below is to get the values for each new student, after the submit button has been pressed

#student_dict will create a dictionary and the key will be your csv column names while the values
#will be the datea gotten from the variables above

#next the student_df is to convert the student_dict to a dataframe

#next we concatenate (join) the old df with student_df. do NOT include the index position in the csv file

if st.button("Submit student scores"):
  students_df = pd.DataFrame({"Name":[name],"Maths":[mat],"English":[eng],"Science":[sci],
                   "Computer Science":[tec],"Average":[average],"Grade":[grade]})
  new_df = pd.concat([df,students_df])
  new_df.to_csv('scores.csv',index=False)
  
  st.success(f"{name}'s total is {total}. The average is {average} and the grade is {grade}")