# create an app for your friends on how much they know you or know something or general quiz
# asks the user to enter his/her name on the questionnaire page
# the questionnaire page can be arranged in 3 or more columns (use your own ideas(-radio - selecbox))
# a button under after all to submit and this checks the right questions and add the scores and save the user score under the user name

# the other page plots the charts of all users who answered and shows their scores

import streamlit as st
import pandas as pd
import plotly.express as px

csvlink = 'questions.csv'

try:
    questioncsv = pd.read_csv('questions.csv')
except:
    questioncsv = pd.DataFrame()

menu = st.sidebar.selectbox("Menu",['Questions','score data'])

if menu == 'Questions':
    st.title("How much do you know about me")
    name = st.text_input("Enter your name")

    c1,c2,c3 = st.columns(3)
    right = 0

    with c1:
        st.subheader("Music")
        
        ins = st.number_input("How many instruments do I play?",0)
        if ins == 4:
            right +=1
        
        lrn = st.selectbox("What other instrument do I want to learn the most?",["Choose","Drums","Harp",'Trumpet','Saxophone'])
        if lrn == "Drums":
            right +=1
        
        clf = st.selectbox("What's the only clef i can read",["Choose","Treble",'Alto',"Tenor","Bass"])
        if clf == "Treble":
            right +=1
        
        pnk = st.selectbox("Whos my favourite music artist right now?",["Choose",'Tyler the creator','Pinkpantheress','Sabrina carpenter','Newjeans'])
        if pnk == "Pinkpantheress":
            right +=1
        
        cnc = st.number_input("How many concerts have I been to this year",0)
        if cnc == 3:
            right +=1         


    with c2:
        st.subheader("School")

        subj = st.selectbox("What's my favourite subject?",["Choose",'History','Music','PE','Maths','Science','English'])
        if subj == "Music":
            right +=1

        bsubj = st.selectbox("What's my least favourite subject?",["Choose",'History','Music','PE','Maths','Science'])
        if bsubj == "English":
            right +=1

        sci = st.selectbox("What science am I best at?",["Choose","Bio",'Chem',"Physics"])
        if sci == "Chem":
            right +=1
        
        his = st.selectbox("What's my favourite history unit",["Choose",'America','Germany','Russia','China'])
        if his == "Germany":
            right +=1
    
    with c3:
        st.subheader("Personal")

        czd = st.selectbox("What is my chinese zodiac?",["Choose",'Dragon','Dog','Ox','Pig','Snake','Tiger','Goat'])
        if czd == "Tiger":
            right +=1
        
        pts = st.number_input("How many pets have I had in total?",0)
        if pts == 4:
            right +=1
        
        mdnm = st.text_input("What is my middle name?")
        if mdnm == "arwen" or "Arwen":
            right +=1
        
        sbl = st.selectbox("My last name is:",["Choose",'Native american','Colombian','Indian','Portuguese'])
        if sbl == 'portuguese':
            right+=1

    if st.button('submit'):
        if name:
            if lrn != 'Choose' and  clf != 'Choose' and pnk != 'Choose' and bsubj != 'Choose' and sci != 'Choose' and his != 'Choose' and czd != 'Choose' and sbl != "Choose" and ins > 0 and pts > 0 and cnc > 0:
                questions_df=pd.DataFrame({"Name":[name],"Correct answers":[right]})
                new_df = pd.concat([questioncsv,questions_df])
                new_df.to_csv('questions.csv',index=False)
                st.success("Answers submitted!!")
            else:
                st.error("Please answer every question!!")
        else:
            st.error("Please enter your name!!")
    
if menu == "score data":

    graph = st.selectbox('Type',['barchart','piechart'])

    if graph == 'barchart':
        barchart = px.bar(questioncsv, x='Name',y='Correct answers',labels={'index':'Names','0':'Correct answers'})
        st.plotly_chart(barchart)
    elif graph == 'piechart':
        piechart = px.pie(questioncsv,names='Name', values='Correct answers')
        st.plotly_chart(piechart)