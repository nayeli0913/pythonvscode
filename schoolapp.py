import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
sch = pd.read_csv('schoolapp.csv')

menu = st.sidebar.selectbox('Menu',['Application','Database'])

if menu == 'Application':
    st.header('Private school application form')
    c1,c2 = st.columns(2)

    with c1:
        pfn = st.text_input('Parent/Guardian name:',placeholder='First name')
        age = st.selectbox('How old is your child',['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'])
        cfn = st.text_input('Child name:',placeholder='First name')

    with c2:
        pln = st.text_input('ln',placeholder='Last name',label_visibility='hidden')
        cg = st.radio('Child gender:',['Male','Female'],horizontal=True)
        st.write('')
        cln = st.text_input('cln',placeholder='Last name',label_visibility='hidden')

    school = st.text_input('The school they come from:')
    ha1 = st.text_input('Home adress',placeholder='Street adress')
    ha2 = st.text_input('ha2',placeholder='Street adress line 2',label_visibility='collapsed')

    a1,a2 = st.columns(2)

    with a1:
        city = st.text_input('city',placeholder='city',label_visibility='collapsed')
        code = st.text_input('cpde',placeholder='Postal/zip code',label_visibility='collapsed')
    
    with a2:
        region = st.text_input('reg',placeholder='Region',label_visibility='collapsed')
        country = st.selectbox('country',['Hong Kong','Germany'],label_visibility='collapsed')
    
    pn = st.text_input('Phone number',placeholder='#### ####')
    
    if st.button('Submit'):
        schooldf = pd.DataFrame({"Parent/guardian firstname":[pfn],"Parent/guardian lastname":[pln],"Child age":[age],
                                "Child gender":[cg],"Child firstname":[cfn],"Child lastname":[cln],"City":[city],"Region":[region],
                                "Postal/zip code":[code],"Country":[country],"Phone number":[pn]})
        newdf = pd.concat([sch,schooldf],ignore_index=True)
        newdf.to_csv('schoolapp.csv',index=False)
        st.success('Application registered')

if menu == 'Database':
    correctpass = "1123"
    
    passw = st.sidebar.text_input('Please input password',type='password')
    login = st.sidebar.button('Login')

    if login:
        if passw:
            if passw == correctpass:
                st.dataframe(sch)
            else:
                st.sidebar.error('Incorrect password')
        else:
            st.sidebar.error('Please enter a password')