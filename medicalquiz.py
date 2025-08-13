import streamlit as st
#https://stemhackathon.com/question-16-medical-quiz/
st.set_page_config(layout='wide',page_title='Medical quiz')

#session state is a permanent storage (dictionary) for streamlit
if 'screenpage' not in st.session_state:
    st.session_state.screenpage = 'homepage'

if 'option' not in st.session_state:
    st.session_state.option = {}

if 'scores' not in st.session_state:
    st.session_state.scores = {}

st.write(st.session_state.scores)
st.write(st.session_state.option)
def homepage():
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    col1a,col2a,col3a = st.columns([1.4,2,1])
    
    with col2a:
        st.title(':blue[Medical Awareness Quiz]')
    
    col1,col2,col3 = st.columns([1,2,1])

    with col2:
        name = st.text_input('Enter your name here',placeholder="name",label_visibility='collapsed')
        if st.pills("Let's get started",["Get started"],label_visibility='collapsed'):
            if name:
                st.session_state.screenpage = 'q1'
                st.rerun()
            else:
                st.error('You have a name.. right?')

def q1(): #fix the button when nothing chosen, it still writes 0 in the score dict. use if qs1: to check if option chosen
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 1]')
        qs1 = st.pills('What is the main job of your heart?',['Pumping blood','Digesting food','Storing energy','Releasing C02'])

        try:
            st.info(f"Option chosen: {st.session_state.option['qs1']}")
        except:
            pass

        if st.button('Next question',key='1b'):

            if 'qs1' in st.session_state.option:
                if qs1:
                    st.session_state.option['qs1'] = qs1
                else:
                    pass
            else:
                st.session_state.option['qs1'] = qs1
    
            if 'qs1' in st.session_state.scores:
                if qs1 == 'Pumping blood':
                    st.session_state.scores['qs1'] = 1
                else:
                    st.session_state.scores['qs1'] = 0
            else:
                if qs1 == 'Pumping blood':
                    st.session_state.scores['qs1'] = 1
                else:
                    st.session_state.scores['qs1'] = 0


            st.session_state.screenpage = 'q2'
            st.rerun()


def q2():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 2]')
        qs2 = st.pills('What do vaccines help protect you from?',['Skin irritation','Diseases like measles and flu','Cuts and bruises','Infections'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs2']}")
        except:
            pass

        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='2a'):
                if 'qs2' in st.session_state.option:
                    pass
                else:
                    st.session_state.option['qs2'] = qs2
                st.session_state.screenpage = 'q1'
                st.rerun()
        with but2:
            if st.button('Next question',key='2b'):
                if 'qs2' in st.session_state.option:
                    pass
                else:
                    st.session_state.option['qs2'] = qs2
                st.session_state.screenpage = 'q3'
                st.rerun()

def q3():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 3]')
        qs3 = st.pills('Why is it important to wash your hands?',['To smell nice','To make them smooth','To look clean','To kill germs on them'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs3']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='3a'):
                st.session_state.option['qs3'] = qs3
                st.session_state.screenpage = 'q2'
                st.rerun()
        with but2:
            if st.button('Next question',key='3b'):
                st.session_state.option['qs3'] = qs3
                st.session_state.screenpage = 'q4'
                st.rerun()

def q4():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 4]')
        qs4 = st.pills('What should you do if you have a fever?',['Play with your friends','Get some rest','Eat a lot','Stay up late'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs4']}")
        except:
            pass

        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='4a'):
                st.session_state.option['qs4'] = qs4
                st.session_state.screenpage = 'q3'
                st.rerun()
        with but2:
            if st.button('Next question',key='4b'):
                st.session_state.option['qs4'] = qs4
                st.session_state.screenpage = 'q5'
                st.rerun()

def q5():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 5]')
        qs5 = st.pills('What does a doctor do?',['Fix cars','Help people stay healthy','Teach math','Sell food'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs5']}")
        except:
            pass

        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='5a'):
                st.session_state.option['qs5'] = qs5
                st.session_state.screenpage = 'q4'
                st.rerun()
        with but2:
            if st.button('Next question',key='5b'):
                st.session_state.option['qs5'] = qs5
                st.session_state.screenpage = 'q6'
                st.rerun()

def q6():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 6]')
        qs6 = st.pills('What is a healthy snack?',['Candy','Soda','Chips','Fruits'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs6']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='6a'):
                st.session_state.option['qs6'] = qs6
                st.session_state.screenpage = 'q5'
                st.rerun()
        with but2:
            if st.button('Next question',key='6b'):
                st.session_state.option['qs6'] = qs6
                st.session_state.screenpage = 'q7'
                st.rerun()

def q7():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 7]')
        qs7 = st.pills('What does it mean to be allergic to something?',['You like it a lot','You cant eat it','Your body reacts to it','You dont like it'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs7']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='7a'):
                st.session_state.option['qs7'] = qs7
                st.session_state.screenpage = 'q6'
                st.rerun()
        with but2:
            if st.button('Next question',key='7b'):
                st.session_state.option['qs7'] = qs7
                st.session_state.screenpage = 'q8'
                st.rerun()

def q8():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 8]')
        qs8 = st.pills('What should you do if you get a cut?',['Ignore it','Wash it and put a bandage on it','Show it to your friends','Lick it'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs8']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='8a'):
                st.session_state.option['qs8'] = qs8
                st.session_state.screenpage = 'q7'
                st.rerun()
        with but2:
            if st.button('Next question',key='8b'):
                st.session_state.option['qs8'] = qs8
                st.session_state.screenpage = 'q9'
                st.rerun()

def q9():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 9]')
        qs9 = st.pills('Why is it important to eat breakfast?',['Its the best meal of the day','It gives you energy for school','pancakes are your favourite','Its not, you can skip it'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs9']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='9a'):
                st.session_state.option['qs9'] = qs9
                st.session_state.screenpage = 'q8'
                st.rerun()
        with but2:
            if st.button('Next question',key='9b'):
                st.session_state.option['qs9'] = qs9
                st.session_state.screenpage = 'q10'
                st.rerun()

def q10():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 10]')
        qs10 = st.pills('How can you keep your bones strong?',['Drink milk','Eat dairy','Take lots of vitamin D','All of the above'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs10']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='10a'):
                st.session_state.option['qs10'] = qs10
                st.session_state.screenpage = 'q9'
                st.rerun()
        with but2:
            if st.button('Next question',key='10b'):
                st.session_state.option['qs10'] = qs10
                st.session_state.screenpage = 'q11'
                st.rerun()

def q11():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 11]')
        qs11 = st.pills('What is the purpose of first aid?',['To help with homework','To give immediate care in emergencies','To prepare healthy food','To provide people medicine'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs11']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='11a'):
                st.session_state.option['qs11'] = qs11
                st.session_state.screenpage = 'q10'
                st.rerun()
        with but2:
            if st.button('Next question',key='11b'):
                st.session_state.option['qs11'] = qs11
                st.session_state.screenpage = 'q12'
                st.rerun()

def q12():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 12]')
        qs12 = st.pills('What helps soothe a sore throat?',['Eating ice cream','Drinking warm fluids','Eating spicy food','Talking a lot'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs12']}")
        except:
            pass

        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='12a'):
                st.session_state.option['qs12'] = qs12
                st.session_state.screenpage = 'q11'
                st.rerun()
        with but2:
            if st.button('Next question',key='12b'):
                st.session_state.option['qs12'] = qs12
                st.session_state.screenpage = 'q13'
                st.rerun()

def q13():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 13]')
        qs13 = st.pills('What is a common cold symptom?',['Runny nose','Aching muscles','Nosebleeds','Trouble moving'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs13']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='13a'):
                st.session_state.option['qs13'] = qs13
                st.session_state.screenpage = 'q12'
                st.rerun()
        with but2:
            if st.button('Next question',key='13b'):
                st.session_state.option['qs13'] = qs13
                st.session_state.screenpage = 'q14'
                st.rerun()

def q14():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 14]')
        qs14 = st.pills('Why should you cover your mouth when you cough/sneeze?',['To be funny','To make the sound quieter','To get your hands dirty','To prevent spraying germs'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs14']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='14a'):
                st.session_state.option['qs14'] = qs14
                st.session_state.screenpage = 'q13'
                st.rerun()
        with but2:
            if st.button('Next question',key='14b'):
                st.session_state.option['qs14'] = qs14
                st.session_state.screenpage = 'q15'
                st.rerun()

def q15():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 15]')
        qs15 = st.pills('What is a safe way to exercise?',['Playing sports','Jumping on the bed','Sitting and reading','None of the above'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs15']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='15a'):
                st.session_state.option['qs15'] = qs15
                st.session_state.screenpage = 'q14'
                st.rerun()
        with but2:
            if st.button('Next question',key='15b'):
                st.session_state.option['qs15'] = qs15
                st.session_state.screenpage = 'q16'
                st.rerun()

def q16():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 16]')
        qs16 = st.pills('What does a dentist check',['Your eyes','Your blood','Your teeth','Your muscles'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs16']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='16a'):
                st.session_state.option['qs16'] = qs16
                st.session_state.screenpage = 'q15'
                st.rerun()
        with but2:
            if st.button('Next question',key='16b'):
                st.session_state.option['qs16'] = qs16
                st.session_state.screenpage = 'q17'
                st.rerun()

def q17():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 17]')
        qs17 = st.pills('What should you do if you feel dizzy?',['Start running','Sit down and tell an adult','Bang your head on the wall','Eat more'])
        but1,but2,space = st.columns([1,1,1.5])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs17']}")
        except:
            pass
        
        with but1:
            if st.button('Prev question',key='17a'):
                st.session_state.option['qs17'] = qs17
                st.session_state.screenpage = 'q16'
                st.rerun()
        with but2:
            if st.button('Next question',key='17b'):
                st.session_state.option['qs17'] = qs17
                st.session_state.screenpage = 'q18'
                st.rerun()

def q18():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 18]')
        qs18 = st.pills('What is the main job of your lungs?',['To pump blood','To digest food','To help you breathe','To carry our respiration'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs18']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='18a'):
                st.session_state.option['qs18'] = qs18
                st.session_state.screenpage = 'q17'
                st.rerun()
        with but2:
            if st.button('Next question',key='18b'):
                st.session_state.option['qs18'] = qs18
                st.session_state.screenpage = 'q19'
                st.rerun()

def q19():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 19]')
        qs19 = st.pills('What can help you stay healthy during cold and flu season?',['Washing hands frequently','Sleeping less','Playing outside everyday','Seeing your friends more often'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs19']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='19a'):
                st.session_state.option['qs19'] = qs19
                st.session_state.screenpage = 'q18'
                st.rerun()
        with but2:
            if st.button('Next question',key='19b'):
                st.session_state.option['qs19'] = qs19
                st.session_state.screenpage = 'q20'
                st.rerun()

def q20():
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.subheader(':red[Question 20]')
        qs20 = st.pills('What does it mean if someone has a headache?',['They are sleepy','They need rest and/or water','They want to play','They need to wear a hat'])
        
        try:
            st.info(f"Option chosen: {st.session_state.option['qs20']}")
        except:
            pass
        
        but1,but2,space = st.columns([1,1,1.5])
        with but1:
            if st.button('Prev question',key='20a'):
                st.session_state.option['qs10'] = qs20
                st.session_state.screenpage = 'q19'
                st.rerun()
        with but2:
            if st.button(':green[Submit]'):
                pass




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
