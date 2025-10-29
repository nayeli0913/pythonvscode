import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF 
import base64
# https://stemhackathon.com/question-16-medical-quiz/
st.set_page_config(layout='wide', page_title='Medical quiz')

menu = st.sidebar.selectbox('Menu',['Quiz','Quiz chart'])

try:
    df = pd.read_csv('medicalquiz.csv')
except:
    df = pd.DataFrame()

# Session state is a permanent storage (dictionary) for Streamlit
if 'screenpage' not in st.session_state:
    st.session_state.screenpage = 'homepage'


if 'option' not in st.session_state:
    st.session_state.option = {}


if 'score' not in st.session_state:
    st.session_state.score = {}


#st.write(st.session_state)

if menu == 'Quiz chart':
    st.table(df)

if menu == 'Quiz':

    def homepage():
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        col1a, col2a, col3a = st.columns([1.4, 2, 1])

        with col2a:
            st.title(':blue[Medical Awareness Quiz]')

        col1, col2, col3 = st.columns([1, 2, 1])


        with col2:
            st.session_state.name = st.text_input('Enter your name here', placeholder="name", label_visibility='collapsed')

            if st.button("Let's get started"):
                if st.session_state.name:
                    st.session_state.screenpage = 'q1'
                    st.rerun()
                else:
                    st.error('You have a name.. right?')


    def q1():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 1]')
            qs1 = st.pills('What is the main job of your heart?', ['Pumping blood', 'Digesting food', 'Storing energy', 'Releasing CO2'])


        if 'qs1' in st.session_state.option:
            if qs1:
                st.session_state.option['qs1'] = qs1
        else:
            st.session_state.option['qs1'] = qs1


        try:
            st.info(f"Option chosen: {st.session_state.option['qs1']}")
        except:
            pass


        if st.button('Next question', key='1b'):
            st.session_state.screenpage = 'q2'
            st.rerun()


    def q2():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 2]')
            qs2 = st.pills('What do vaccines help protect you from?', ['Skin irritation', 'Diseases like measles and flu', 'Cuts and bruises', 'Infections'])
            
            if 'qs2' in st.session_state.option:
                if qs2:
                    st.session_state.option['qs2'] = qs2
            else:
                st.session_state.option['qs2'] = qs2


        try:
            st.info(f"Option chosen: {st.session_state.option['qs2']}")
        except:
            pass


        but1, but2, space = st.columns([1, 1, 1.5])
        with but1:
            if st.button('Prev question', key='2a'):
                st.session_state.screenpage = 'q1'
                st.rerun()
        with but2:
            if st.button('Next question', key='2b'):
                st.session_state.screenpage = 'q3'
                st.rerun()


    def q3():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 3]')
            qs3 = st.pills('Why is it important to wash your hands?', ['To smell nice', 'To make them smooth', 'To look clean', 'To kill germs on them'])
            
            if 'qs3' in st.session_state.option:
                if qs3:
                    st.session_state.option['qs3'] = qs3
            else:
                st.session_state.option['qs3'] = qs3


        try:
            st.info(f"Option chosen: {st.session_state.option['qs3']}")
        except:
            pass
        
        but1, but2, space = st.columns([1, 1, 1.5])
        with but1:
            if st.button('Prev question', key='3a'):
                st.session_state.screenpage = 'q2'
                st.rerun()
        with but2:
            if st.button('Next question', key='3b'):
                st.session_state.screenpage = 'q4'
                st.rerun()


    def q4():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 4]')
            qs4 = st.pills('What should you do if you have a fever?', ['Play with your friends', 'Get some rest', 'Eat a lot', 'Stay up late'])
            
            if 'qs4' in st.session_state.option:
                if qs4:
                    st.session_state.option['qs4'] = qs4
            else:
                st.session_state.option['qs4'] = qs4


        try:
            st.info(f"Option chosen: {st.session_state.option['qs4']}")
        except:
            pass


        but1, but2, space = st.columns([1, 1, 1.5])
        with but1:
            if st.button('Prev question', key='4a'):
                st.session_state.screenpage = 'q3'
                st.rerun()
        with but2:
            if st.button('Next question', key='4b'):
                st.session_state.screenpage = 'q5'
                st.rerun()


    def q5():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 5]')
            qs5 = st.pills('What does a doctor do?', ['Fix cars', 'Help people stay healthy', 'Teach math', 'Sell food'])
            
            if 'qs5' in st.session_state.option:
                if qs5:
                    st.session_state.option['qs5'] = qs5
            else:
                st.session_state.option['qs5'] = qs5


        try:
            st.info(f"Option chosen: {st.session_state.option['qs5']}")
        except:
            pass


        but1, but2, space = st.columns([1, 1, 1.5])
        with but1:
            if st.button('Prev question', key='5a'):
                st.session_state.screenpage = 'q4'
                st.rerun()
        with but2:
            if st.button('Next question', key='5b'):
                st.session_state.screenpage = 'q6'
                st.rerun()


    def q6():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 6]')
            qs6 = st.pills('Which of these is a healthy snack?', ['Candy', 'Soda', 'Chips', 'Fruits'])
            
            if 'qs6' in st.session_state.option:
                if qs6:
                    st.session_state.option['qs6'] = qs6
            else:
                st.session_state.option['qs6'] = qs6


        try:
            st.info(f"Option chosen: {st.session_state.option['qs6']}")
        except:
            pass


        but1, but2, space = st.columns([1, 1, 1.5])
        with but1:
            if st.button('Prev question', key='6a'):
                st.session_state.screenpage = 'q5'
                st.rerun()
        with but2:
            if st.button('Next question', key='6b'):
                st.session_state.screenpage = 'q7'
                st.rerun()


    def q7():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 7]')
            qs7 = st.pills('What does it mean to be allergic to something?', ['You like it a lot', 'You cant digest it', 'Your body reacts to it', 'You dont like it'])

            if 'qs7' in st.session_state.option:
                if qs7:
                    st.session_state.option['qs7'] = qs7
            else:
                st.session_state.option['qs7'] = qs7


            try:
                st.info(f"Option chosen: {st.session_state.option['qs7']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='7a'):
                    st.session_state.screenpage = 'q6'
                    st.rerun()
            with but2:
                if st.button('Next question', key='7b'):
                    st.session_state.screenpage = 'q8'
                    st.rerun()


    def q8():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 8]')
            qs8 = st.pills('What should you do FIRST if you get a cut?', ['Ignore it', 'Wash and clean it', 'Put a bandaid on it', 'Lick it'])

            if 'qs8' in st.session_state.option:
                if qs8:
                    st.session_state.option['qs8'] = qs8
            else:
                st.session_state.option['qs8'] = qs8

            try:
                st.info(f"Option chosen: {st.session_state.option['qs8']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='8a'):
                    st.session_state.screenpage = 'q7'
                    st.rerun()
            with but2:
                if st.button('Next question', key='8b'):
                    st.session_state.screenpage = 'q9'
                    st.rerun()


    def q9():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 9]')
            qs9 = st.pills('Why is it important to eat breakfast?', ['It’s the best meal of the day', 'It gives you energy for school', 'Pancakes are your favorite', 'It’s not, you can skip it'])

            if 'qs9' in st.session_state.option:
                if qs9:
                    st.session_state.option['qs9'] = qs9
            else:
                st.session_state.option['qs9'] = qs9


            try:
                st.info(f"Option chosen: {st.session_state.option['qs9']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='9a'):
                    st.session_state.screenpage = 'q8'
                    st.rerun()
            with but2:
                if st.button('Next question', key='9b'):
                    st.session_state.screenpage = 'q10'
                    st.rerun()


    def q10():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 10]')
            qs10 = st.pills('How can you keep your bones strong?', ['Drink milk', 'Eat dairy', 'Take lots of vitamin D', 'All of the above'])

            if 'qs10' in st.session_state.option:
                if qs10:
                    st.session_state.option['qs10'] = qs10
            else:
                st.session_state.option['qs10'] = qs10


            try:
                st.info(f"Option chosen: {st.session_state.option['qs10']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='10a'):
                    st.session_state.screenpage = 'q9'
                    st.rerun()
            with but2:
                if st.button('Next question', key='10b'):
                    st.session_state.screenpage = 'q11'
                    st.rerun()


    def q11():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 11]')
            qs11 = st.pills('What is the purpose of first aid?', ['To help with homework', 'To give immediate care in emergencies', 'To prepare healthy food', 'To provide people medicine'])

            if 'qs11' in st.session_state.option:
                if qs11:
                    st.session_state.option['qs11'] = qs11
            else:
                st.session_state.option['qs11'] = qs11


            try:
                st.info(f"Option chosen: {st.session_state.option['qs11']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='11a'):
                    st.session_state.screenpage = 'q10'
                    st.rerun()
            with but2:
                if st.button('Next question', key='11b'):
                    st.session_state.screenpage = 'q12'
                    st.rerun()


    def q12():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 12]')
            qs12 = st.pills('What helps soothe a sore throat?', ['Ice cream', 'Warm drinks', 'Spicy food', 'Talking a lot'])

            if 'qs12' in st.session_state.option:
                if qs12:
                    st.session_state.option['qs12'] = qs12
            else:
                st.session_state.option['qs12'] = qs12


            try:
                st.info(f"Option chosen: {st.session_state.option['qs12']}")
            except:
                pass


            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='12a'):
                    st.session_state.screenpage = 'q11'
                    st.rerun()
            with but2:
                if st.button('Next question', key='12b'):
                    st.session_state.screenpage = 'q13'
                    st.rerun()


    def q13():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 13]')
            qs13 = st.pills('What is a common cold symptom?', ['Runny nose', 'Aching muscles', 'Nosebleeds', 'Trouble moving'])

            if 'qs13' in st.session_state.option:
                if qs13:
                    st.session_state.option['qs13'] = qs13
            else:
                st.session_state.option['qs13'] = qs13


            try:
                st.info(f"Option chosen: {st.session_state.option['qs13']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='13a'):
                    st.session_state.screenpage = 'q12'
                    st.rerun()
            with but2:
                if st.button('Next question', key='13b'):
                    st.session_state.screenpage = 'q14'
                    st.rerun()


    def q14():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 14]')
            qs14 = st.pills('Why should you cover your mouth when you cough/sneeze?', ['To be funny', 'To make the sound quieter', 'To get your hands dirty', 'To prevent spreading germs'])

            if 'qs14' in st.session_state.option:
                if qs14:
                    st.session_state.option['qs14'] = qs14
            else:
                st.session_state.option['qs14'] = qs14


            try:
                st.info(f"Option chosen: {st.session_state.option['qs14']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='14a'):
                    st.session_state.screenpage = 'q13'
                    st.rerun()
            with but2:
                if st.button('Next question', key='14b'):
                    st.session_state.screenpage = 'q15'
                    st.rerun()


    def q15():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 15]')
            qs15 = st.pills('What is a safe way to exercise?', ['Playing sports', 'Jumping on the bed', 'Sitting and reading', 'Biking on the road'])

            if 'qs15' in st.session_state.option:
                if qs15:
                    st.session_state.option['qs15'] = qs15
            else:
                st.session_state.option['qs15'] = qs15


            try:
                st.info(f"Option chosen: {st.session_state.option['qs15']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='15a'):
                    st.session_state.screenpage = 'q14'
                    st.rerun()
            with but2:
                if st.button('Next question', key='15b'):
                    st.session_state.screenpage = 'q16'
                    st.rerun()


    def q16():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 16]')
            qs16 = st.pills('What does a dentist check?', ['Your eyes', 'Your blood', 'Your teeth', 'Your muscles'])

            if 'qs16' in st.session_state.option:
                if qs16:
                    st.session_state.option['qs16'] = qs16
            else:
                st.session_state.option['qs16'] = qs16


            try:
                st.info(f"Option chosen: {st.session_state.option['qs16']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='16a'):
                    st.session_state.screenpage = 'q15'
                    st.rerun()
            with but2:
                if st.button('Next question', key='16b'):
                    st.session_state.screenpage = 'q17'
                    st.rerun()


    def q17():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 17]')
            qs17 = st.pills('What should you do if you feel dizzy?', ['Start running', 'Sit down and tell an adult', 'Bang your head on the wall', 'Eat more'])

            if 'qs17' in st.session_state.option:
                if qs17:
                    st.session_state.option['qs17'] = qs17
            else:
                st.session_state.option['qs17'] = qs17


            try:
                st.info(f"Option chosen: {st.session_state.option['qs17']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='17a'):
                    st.session_state.screenpage = 'q16'
                    st.rerun()
            with but2:
                if st.button('Next question', key='17b'):
                    st.session_state.screenpage = 'q18'
                    st.rerun()


    def q18():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 18]')
            qs18 = st.pills('What process occurs in the lungs?', ['Digestion', 'Respiration', 'Photosynthesis', 'Ventilation'])

            if 'qs18' in st.session_state.option:
                if qs18:
                    st.session_state.option['qs18'] = qs18
            else:
                st.session_state.option['qs18'] = qs18


            try:
                st.info(f"Option chosen: {st.session_state.option['qs18']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='18a'):
                    st.session_state.screenpage = 'q17'
                    st.rerun()
            with but2:
                if st.button('Next question', key='18b'):
                    st.session_state.screenpage = 'q19'
                    st.rerun()


    def q19():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 19]')
            qs19 = st.pills('What can help you stay healthy during cold and flu season?', ['Washing your hands frequently', 'Sleeping more', 'Playing outside every day', 'Seeing your friends more often'])

            if 'qs19' in st.session_state.option:
                if qs19:
                    st.session_state.option['qs19'] = qs19
            else:
                st.session_state.option['qs19'] = qs19


            try:
                st.info(f"Option chosen: {st.session_state.option['qs19']}")
            except:
                pass

            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='19a'):
                    st.session_state.screenpage = 'q18'
                    st.rerun()
            with but2:
                if st.button('Next question', key='19b'):
                    st.session_state.screenpage = 'q20'
                    st.rerun()


    def q20():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.subheader(':red[Question 20]')
            qs20 = st.pills('What does it mean if someone has a headache?', ['They are sleepy', 'They need rest and/or water', 'They want to play', 'They need to wear a hat'])

            if 'qs20' in st.session_state.option:
                if qs20:
                    st.session_state.option['qs20'] = qs20
            else:
                st.session_state.option['qs20'] = qs20


            try:
                st.info(f"Option chosen: {st.session_state.option['qs20']}")
            except:
                pass
            
            but1, but2, space = st.columns([1, 1, 1.5])
            with but1:
                if st.button('Prev question', key='20a'):
                    st.session_state.screenpage = 'q19'
                    st.rerun()
            with but2:
                if st.button(':green[Review Questions]'):
                    st.session_state.screenpage = 'review'
                    st.rerun()

    certificate = 'certificate.png'

    def generatepdf():
        pdf = FPDF(orientation='L')

        pdf.add_page()

        xpos = 20
        ypos = 30
        colw = 90

        pdf.image(certificate,x=0,y=0,w=300,h=220)

        pdf.set_font(family='Courier',size=50,style='B')
        pdf.set_xy(x=110,y=110)
        pdf.cell(w=colw,txt=f'{st.session_state.name}', ln=True, align='C')

        pdf.set_font(family='Courier',size=80,style='B')
        pdf.set_xy(x=148,y=170)
        pdf.cell(w=colw,txt=f'{st.session_state.percent}%',ln=True)

        pdf_file = 'certificate.pdf'
        pdf.output(pdf_file)
        return pdf_file

    def review():
        st.info(f'{st.session_state.name} you can review your quiz')

        queslist = ['qs1','qs2','qs3','qs4','qs5','qs6','qs7','qs8','qs9','qs10','qs11','qs12','qs13','qs14','qs15','qs16','qs17','qs18','qs19','qs20']

        notans = []
        for ques in queslist:
            if st.session_state.option[ques] == None:
                notans.append(int(ques[2:]))
        st.error(f'Questions {notans} not yet answered')


        but1, but2, space = st.columns([1, 3, 1.5])
        with but1:
            if st.button('Prev question', key='20c'):
                st.session_state.screenpage = 'q20'
                st.rerun()
        with but2:
            submit = st.pills(':rainbow[Submit Now]',[':rainbow[Submit now]'],label_visibility='collapsed')

        if submit:
            if st.session_state.option['qs1'] == 'Pumping blood':
                st.session_state.score['qs1'] = 1
            if st.session_state.option['qs2'] == 'Diseases like measles and flu':
                st.session_state.score['qs2'] = 1
            if st.session_state.option['qs3'] == 'To kill germs on them':
                st.session_state.score['qs3'] = 1
            if st.session_state.option['qs4'] == 'Get some rest':
                st.session_state.score['qs4'] = 1
            if st.session_state.option['qs5'] == 'Help people stay healthy':
                st.session_state.score['qs5'] = 1
            if st.session_state.option['qs6'] == 'Fruits':
                st.session_state.score['qs6'] = 1
            if st.session_state.option['qs7'] == 'Your body reacts to it':
                st.session_state.score['qs7'] = 1
            if st.session_state.option['qs8'] == 'Wash and clean it':
                st.session_state.score['qs8'] = 1
            if st.session_state.option['qs9'] == 'It gives you energy for school':
                st.session_state.score['qs9'] = 1
            if st.session_state.option['qs10'] == 'All of the above':
                st.session_state.score['qs10'] = 1

            if st.session_state.option['qs11'] == 'To give immediate care in emergencies':
                st.session_state.score['qs11'] = 1
            if st.session_state.option['qs12'] == 'Warm drinks':
                st.session_state.score['qs12'] = 1
            if st.session_state.option['qs13'] == 'Runny nose':
                st.session_state.score['qs13'] = 1
            if st.session_state.option['qs14'] == 'To prevent spreading germs':
                st.session_state.score['qs14'] = 1
            if st.session_state.option['qs15'] == 'Playing sports':
                st.session_state.score['qs15'] = 1
            if st.session_state.option['qs16'] == 'Your teeth':
                st.session_state.score['qs16'] = 1
            if st.session_state.option['qs17'] == 'Sit down and tell an adult':
                st.session_state.score['qs17'] = 1
            if st.session_state.option['qs18'] == 'Ventilation':
                st.session_state.score['qs18'] = 1
            if st.session_state.option['qs19'] == 'Wash your hands frequently':
                st.session_state.score['qs19'] = 1
            if st.session_state.option['qs20'] == 'They need rest and/or water':
                st.session_state.score['qs20'] = 1

            points = sum(st.session_state.score.values())
            st.session_state.percent = int(points/20 * 100)
            st.info(f'Your final score is {points} out of 20')

            medicaldf = pd.DataFrame({"Name":[st.session_state.name],"Final score":[points]})
            newdf = pd.concat([df,medicaldf],ignore_index=True)
            newdf.to_csv('medicalquiz.csv',index=False)

            callpdf = generatepdf()
            with open(callpdf,'rb') as genpdf:
                readpdf = genpdf.read()

            write_pdf = base64.b64encode(readpdf).decode('utf-8')
            embed_pdf = f'<embed src="data:application/pdf;base64, {write_pdf}" type="application/pdf" width = "70%" height="600px" />'
            st.markdown(embed_pdf,unsafe_allow_html=True)

            with but1:
                st.download_button(label='Download certificate',data=readpdf,file_name="Medicalquizcertificate.pdf",mime='application/pdf')

            #barchart = px.bar(st.session_state.name, x='index',y=0,labels={'index':'Name','0':''})
            #st.plotly_chart(barchart)





    # Main navigation
    if st.session_state.screenpage == 'homepage':
        homepage()
    elif st.session_state.screenpage == 'q1':
        q1()
    elif st.session_state.screenpage == 'q2':
        q2()
    elif st.session_state.screenpage == 'q3':
        q3()
    elif st.session_state.screenpage == 'q4':
        q4()
    elif st.session_state.screenpage == 'q5':
        q5()
    elif st.session_state.screenpage == 'q6':
        q6()
    elif st.session_state.screenpage == 'q7':
        q7()
    elif st.session_state.screenpage == 'q8':
        q8()
    elif st.session_state.screenpage == 'q9':
        q9()
    elif st.session_state.screenpage == 'q10':
        q10()
    elif st.session_state.screenpage == 'q11':
        q11()
    elif st.session_state.screenpage == 'q12':
        q12()
    elif st.session_state.screenpage == 'q13':
        q13()
    elif st.session_state.screenpage == 'q14':
        q14()
    elif st.session_state.screenpage == 'q15':
        q15()
    elif st.session_state.screenpage == 'q16':
        q16()
    elif st.session_state.screenpage == 'q17':
        q17()
    elif st.session_state.screenpage == 'q18':
        q18()
    elif st.session_state.screenpage == 'q19':
        q19()
    elif st.session_state.screenpage == 'q20':
        q20()
    elif st.session_state.screenpage == 'review':
        review()
