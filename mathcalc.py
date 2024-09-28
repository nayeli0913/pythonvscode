import streamlit as st

st.header("number calculator")
st.image("https://www.autodesk.com/products/fusion-360/blog/wp-content/uploads/2023/03/calculator-gdc0b8a6a8_1920.jpg")

n1 = st.number_input("Enter a number")
n2 = st.number_input("Enter another number")
act = st.selectbox("",['Add','Subtract','Multiply','Divide'])

if st.button("Enter"):
    if act == 'Add':
        st.subheader(n1+n2)
    elif act == 'Subtract':
        st.subheader(n1-n2)
    elif act == 'Multiply':
        st.subheader(n1*n2)
    else:
        st.subheader(n1/n2)