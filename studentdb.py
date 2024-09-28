#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -save and update in a csv file



import streamlit as st

import pandas as pd


import plotly.express as px

st.set_page_config(layout='wide',page_title='Student Database',page_icon='😮')
df = pd.read_csv('scores.csv')
#csv file is a text file where each data is seperated by a comma (comma seperated value)

studentID = 'Student '+ str(len(df) + 1)

menu = st.sidebar.selectbox('Menu',['Submit', 'Table and chart','Student file'])

if menu =='Submit':

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
    hist = st.number_input("Enter your history score")

  average = (hist+sci+eng+mat)/4

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

  total = mat+sci+hist+eng

  #this function below is to get the values for each new student, after the submit button has been pressed

  #student_dict will create a dictionary and the key will be your csv column names while the values
  #will be the datea gotten from the variables above

  #next the student_df is to convert the student_dict to a dataframe

  #next we concatenate (join) the old df with student_df. do NOT include the index position in the csv file

  if st.button("Submit student scores"):
    students_df = pd.DataFrame({"Student ID":[studentID],"Name":[name],"Maths":[mat],"English":[eng],"Science":[sci],
                    "History":[hist],"Average":[average],"Grade":[grade]})
    new_df = pd.concat([df,students_df])
    new_df.to_csv('scores.csv',index=False)
    
    st.success(f"{name}'s total is {total}. The average is {average} and the grade is {grade}")

if menu == 'Table and chart':

  #download csv file
  with open('scores.csv') as file: #open to make file readable as each character
    data = file.read() #read and store content in variable
  st.sidebar.download_button(label='Download Database CSV',data=data,file_name='Student scores database.csv')
  
  with st.expander("Show database"):
    st.table(df)
  subjects = ['Maths','English','Science','History']
  subjectstable = df[subjects].mean().reset_index()

#Bar chart
  barchart= px.bar(subjectstable,x='index', y=0, labels={'index':'subjects','0':'average'})

#Pie chart
  piechart = px.pie(subjectstable,names='index', values=0, labels={'index':'subjects','0':'average'})

  grap = st.radio('Graph',['Bar','Pie'],horizontal=True)
  
  if grap == 'Bar':
    st.plotly_chart(barchart)
  else:
    st.plotly_chart(piechart)

if menu == 'Student file':
  cl1,cl2,cl3 = st.columns(3)
  with cl3:
    findstudent = st.text_input('Enter student ID')
    searchstudent = st.button('Find Student')

  if searchstudent:
     if findstudent:
        searchresult = df[df['Student ID'].str.lower() == findstudent.lower()]
        getname = searchresult['Name'].iloc[0] #get the first item in name column.iloc = index position
        getmath = searchresult['Maths'].iloc[0]
        geteng = searchresult['English'].iloc[0]
        getsci = searchresult ['Science'].iloc[0]
        gethist = searchresult['History'].iloc[0]
        getavg = searchresult['Average'].iloc[0]
        getgrd = searchresult['Grade'].iloc [0]

        p1,p2,p3 = st.columns(3)

        with p1:
          st.header(f':red[{getname}]')
          st.header('Subject list')
          st.write('Math')
          st.write('English')
          st.write('Science')
          st.write('History')
          st.write('Average')
          st.header(f':red[GRADE:] {getgrd}')

        
        with p2:
           st.header('')
           st.header('Score')
           st.write(f'{getmath}')
           st.write(f'{geteng}')
           st.write(f'{getsci}')
           st.write(f'{gethist}')
           st.write(f'{getavg}')
