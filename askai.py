import streamlit as st
import requests

apikey = st.text_input('enter your api') #'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' 
apilink = "https://openrouter.ai/api/v1/chat/completions" #THIS CONNECTS TO OPENROUTER
headers = {'Authorization': f'Bearer {apikey}', 'Content-Type': 'application/json'}

def askai(content):
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

topic = st.sidebar.selectbox('choose a python topic',['variables','lists','functions','dictionaries','while loops','for loops','if else','range'])

explanation = f"""give a breif, concise summary on the python topic {topic} with examples while still keeping it detailed and informative
"""

question = f"""make a multiple choice question on python {topic} without giving the answer"""

generate = st.sidebar.pills('',['Generate topic'])
if generate:
    with st.spinner('Generating..'):
        expinfo = askai(explanation)
        qsinfo = askai(question)
        st.subheader(f'About python {topic}:')
        st.info(expinfo)

        answer = f"""answer this question: {qsinfo}"""
        ansinfo = askai(answer)

        tab1, tab2 = st.tabs(['question','answer'])
        with tab1:
            st.subheader("Question on the topic")
            st.info(qsinfo)
        with tab2:
            st.subheader("Answer")
            st.success(ansinfo)
