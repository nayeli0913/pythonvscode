import streamlit as st
import google.generativeai as genai

st.sidebar.title('AI resume generator')
st.sidebar.write('Fill in your details to generate a good resume')
name = st.sidebar.text_input('Please enter your name')
if st.sidebar.checkbox('Add email'):
    email = st.sidebar.text_input('Please enter your email')
if st.sidebar.checkbox('Add phone number'):
    phone = st.sidebar.text_input('Please enter your phone number')
skills = st.sidebar.text_area('Key skills for your resume',placeholder='eg. Experienced quality control expert')
exp = st.sidebar.text_area('Details about your previous experiences',placeholder='I have worked with samsung TV department for 4 years, etc.')
edu = st.sidebar.text_area('Details about your past education & years',placeholder='eg. Graduated harvard in the class of 2024')

api_key = 'AIzaSyDt1SUOP27V9Caow5tOnWwGvSg0Mn-X_eA'

def configure_ai():
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-pro')

#start our gemin ai
model = configure_ai()

#send the question,orompt cv in the ai

def ai_cv(name,email,phone,skills,exp,edu):

    summary_prompt = f"""
    Extract the informtaion below to create a good composed, comprehensive proffessional summary
    using these information:
    {skills}{exp}
    """

    skills_prompt = f"""
    Extract the information below to create a comprehensive key skils section with complete sentences each of what I can do

    using the key stills here:
    {skills}

    """

    exp_prompt = f"""
    extract the information below to create a comprehensive career experience section with complete sentences of what I've
    achieved at previous jobs.

    using my career experience here:
    {exp}
    """

    edu_prompt = f"""
    extract the information below to create my educational background simply in bullet points
    using my educational background here
    {edu}
    """

    try:
        summarycontent = model.generate_content(summary_prompt)
        summaryreturn = summarycontent.text

        skillscontent = model.generate_content(skills_prompt)
        summaryreturn = skillscontent.text

        educontent = model.generate_content(edu_prompt)
        summaryreturn = educontent.text
        
        expcontent = model.generate_content(exp_prompt)
        summaryreturn = expcontent.text

    except Exception as e:
        st.error(f'Error generating resume: {str(e)}')

if st.sidebar.button('Generate Resume'):
    if name and phone and skills:
        with st.spinner('Processing.. Please wait'):
            updated_cv = ai_cv(name,email,phone,skills,exp,edu)

        if updated_cv:
            st.sidebar.success('Resume generated successfuly')

            st.write(updated_cv)
    else:
        st.sidebar.warning('Please provide resume details')