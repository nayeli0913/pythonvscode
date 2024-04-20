# -tell us what a list is in python
# -create an example of a list and display it in python
# -give 3 examples of how to use a list in streamlit

import streamlit as st

st.write("A list in python is used when multiple data is in one place, for example")

list = ['apple', 'banana', 'orange']
st.write(list)

st.write("There are also other ways to use a list, such as a selectbox or radio")

st.selectbox('Select which fruit',['apple','banana','orange'])

st.radio('Select which fruit',['peach','watermelon','strawberry'])