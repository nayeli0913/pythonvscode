import streamlit as st
import requests #module used to interact with other websitse/apps

#-------------------CONFIGURATIONS------------------------
apikey = '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' 
apilink = "https://openrouter.ai/api/v1/chat/completions" #THIS CONNECTS TO OPENROUTER
headers = {'Authorization': f'Bearer {apikey}', 'Content-Type': 'application/json'}
#----------------------------------------

#-----------Funtion to send a.i prompts-------------------------
def ask_ai(content):
    data = {'model':'openai/gpt-3.5-turbo', 'messages': [{'role': 'user', 'content': content}]}
    response = requests.post(apilink,headers=headers,json=data) #post=send, json is the file 
    return response.json() ['choices'][0] ['message'] ['content'] #waiting for the a.i response
#----------------------------------------

name = st.sidebar.text_input('Full name')
phone = st.sidebar.text_input('Phone number')
home = st.sidebar.text_input('Current country and area of residence')
st.sidebar.divider()

pt = st.sidebar.toggle('Photo (optional)')
if pt:
    photo = st.sidebar.file_uploader('Upload a JPG, PNG, or JPEG image of yourself',type=['JPG','PNG','JPEG'])

emt = st.sidebar.toggle('Email address (optional)')
if emt:
    mail = st.sidebar.text_input('Enter your email address')
st.sidebar.divider()

st.sidebar.subheader('Key skills (one per line)')
skills = st.sidebar.text_area('',label_visibility='collapsed',placeholder=f"""Example: 
Adobe photoshop
Customer service""")

st.sidebar.subheader('Work experience')
workexp = st.sidebar.text_area('',label_visibility='collapsed',placeholder=f"""Example:
Assistant tech officer at Nintendo Japan (2017-2024)""")

st.sidebar.subheader('Education')
edexp = st.sidebar.text_area('',label_visibility='collapsed',placeholder=f"""Example:
Harvard University class of 2022 with a doctorate in computer science (2019-2022)""")

summary = f'''Design a professional summary for my CV. Make it 4-5 lines using the information given below
my key skills: {skills}
my work experience: {workexp}
my education: {edexp}
'''

generate = st.sidebar.button('Generate my CV')
if generate:
    with st.spinner('Generating your cv'):
        if name and phone and home and workexp and edexp and skills:
            summaryresponse = ask_ai(summary)
            st.write(summaryresponse)
