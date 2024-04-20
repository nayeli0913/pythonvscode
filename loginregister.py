#create a register and login side bar to allow many people to register (create their username, password)
#then another page to login checking if their credentials are correct. (login with your username, password)
#display their username after a succesful login

import streamlit as st
import pandas as pd

password = pd.read_csv('loginregister.csv')
menu = st.sidebar.selectbox('Menu',['Register','Login'])

if menu =='Register':
    st.subheader('Register a username and password')
    username = st.text_input('Enter a username')
    passw = st.text_input('Enter a password')

    if st.button('Register'):
      password_dict = {"Username":[username], "Password":[passw]}
      passwordf = pd.DataFrame(password_dict)
      df = pd.concat([password,passwordf],ignore_index=True)
      df.to_csv('loginregister.csv',index=False)
      st.success("User registered")

if menu =='Login':
    st.dataframe(password)
    st.subheader('Login to your account')
    correctuser = password['Username'].iloc[0]
    correctpass = password['Password'].iloc[0]

    userin = st.text_input('Username')
    userpas = st.text_input('Password')

    if st.button('Login'):
      if correctuser == userin and correctpass == userpas:
            st.success(f"Welcome {correctuser}")
      elif correctuser != userin and correctpass == userpas:
        st.error("Username not found")
      elif correctpass != userpas and correctuser == userin:
        st.error("Password doesn't match")
      elif correctuser != userin and correctpass != userpas:
        st.error("Incorrect username and password")