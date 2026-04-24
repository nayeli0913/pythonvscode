import streamlit as st
import requests #module used to interact with other websites/apps


#-------------------CONFIGURATIONS------------------------
apikey = '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'
apilink = "https://openrouter.ai/api/v1/chat/completions" #THIS CONNECTS TO OPENROUTER
headers = {'Authorization': f'Bearer {apikey}', 'Content-Type': 'application/json'}
#----------------------------------------


name = st.sidebar.text_input('Full name')
phone = st.sidebar.text_input('Phone number')
home = st.sidebar.text_input('Current country and area of residence')
st.sidebar.divider()




pt = st.sidebar.toggle('Photo (optional)')
if pt:
    photo = st.sidebar.file_uploader('Upload a JPG, PNG, or JPEG image of yourself',type=['JPG', 'PNG', 'JPEG'])




#-----------Funtion to send a.i prompts-------------------------
def ask_ai(content):
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": content}],
        "max_tokens": 250,
        "temperature": 0.7
    }
    response = requests.post(apilink, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}"


#----------------------------------------


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




#--------------Prompts here-----------------------
#Professional Summary|Key Skills and Experience|Work Experience|Education


summary = f"""Design a professional summary for my CV. Make it 4-5 lines using the information given below:
My key Skills: {skills}
My work experience: {workexp}
My education: {edexp}
"""
skillsp = f""" create a bulleted list with one-line explanations for each skill: {skills}"""

workp = f"""Format work experience as:
company/organisation
start-end date
job title
respisbilites/achievements (bullet pointed):
{workexp}"""

edup = f"""format education as:
course/degree
start-end
school/provider: 
{edexp}"""



#----------------------------------------




generate = st.sidebar.button('Generate my CV')
if generate:
    with st.spinner('Generating your CV'):
        if name and phone and home and workexp and edexp and skills:
            summary_response = ask_ai(summary)
            st.subheader('Professional summary')
            profarea = st.text_area('You can make edits before downloading',value=summary_response,height=200)

            skills_response = ask_ai(skillsp)
            st.subheader('Key skills')
            skillarea = st.text_area('You can make edits before downloading',value=skills_response,height=200)

            exp_response = ask_ai(workp)
            st.subheader('Work experience')
            exparea = st.text_area('You can make edits before downloading',value=exp_response,height=200)

            edu_response = ask_ai(edup)
            st.subheader('Education')
            eduarea = st.text_area('You can make edits before downloading',value=edu_response,height=200)