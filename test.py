import streamlit as st

import pandas as pd

menu = st.sidebar.selectbox('Menu',['Register','Database'])
df = pd.read_csv('test.csv')

c1,c2 = st.columns(2)

if menu == 'Register':
   with c1:
      name = st.text_input('enter your name')

   with c2:
      age = st.number_input('enter your age')

   if st.button('Submit'):
      studentdf = pd.DataFrame({"Name":[name],"Age":[age]})
      newdf = pd.concat([df,studentdf])
      newdf.to_csv('test.csv',index=False)
      st.success('Details saved successfully')

if menu == 'Database':
   st.dataframe(df)