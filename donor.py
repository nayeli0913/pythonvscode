# Create a menu for Registration and Database
# Design a blood donation database that can get donor input
# -Name -Contact Number (use text)
# -Blood group (use radio or selectbox) -Disease/Infection (use radio or selectbox)

# -Submit donor details

# Next, save these in a csv file and show the database in a Database page in the menu

import streamlit as st

import pandas as pd
df = pd.read_csv('donor.csv',dtype={"Contact information":str})

menu = st.sidebar.selectbox('Menu',['Registration','Database'])

if menu == 'Registration':
    st.subheader('Register here')
    c1,c2 = st.columns(2)

    with c1:
        name = st.text_input('Enter your name')
        bloodgroup = st.selectbox('Blood group',['A','B','O','O+','O-'])
    
    with c2:
        contact = st.text_input('Enter your contact number')
        disease = st.selectbox('Do you have a disease?',['Yes','No'])

    if st.button('Submit'):
       donordf = pd.DataFrame({"Name":[name],"Contact information":[contact],"Blood group":[bloodgroup],"Disease present":[disease]})
       newdf = pd.concat([df,donordf])
       newdf.to_csv('donor.csv',index=False)
       st.success("Donor registered")

if menu == 'Database':
    st.dataframe(df)