import streamlit as st

apikey = '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'
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

topic = st.selectbox('choose a python topic',['variables','lists','functions','dictionaries'])

explanation = f"""give a breif, concise summary on the python topic {topic} with examples while still keeping it detailed and informative
"""

question = f"""make a multiple choice question on python {topic} without giving the answer"""

generate = st.pills('',['Generate topic'])
if generate:
    with st.spinner('Generating..')
    expinfo = askai(explanation)
    qsinfo = askai(question)
    st.subheader(f'about python {topic}:')
    st.success(expinfo)

    answer = f"""answer this question: {qsinfo}"""
    ansinfo = askai(answer)

    tab1, tab2, st.tabs{['question','answer']}
    with tab1:
        st.subheader("Question on the topic")
        st.info(qsinfo)
    with tab2:
        st.subheader("Answer")
        st.info(ansinfo)
