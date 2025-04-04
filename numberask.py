# Write  a program to ask the user to enter two separate numbers, the start number and the finish number.  -10marks
# check how  many odd numbers and even numbers that are in between the specified numbers the user requested - 50marks
# - display all the even number and also the odd numbers as well (skip) -10marks

# #-Put a check that the start number cannot be greater or equal to the end number -10marks
# #-put a notification that the user cannot enter a letter (alert if he does) -20marks


import streamlit as st
evenlist=[]
oddlist = []

first = st.number_input('Enter the first number')
last = st.number_input('Enter the last number')

for number in range(first, last+1):
    if number % 2 == 0:
        evenlist.append(number)
    else:
        oddlist.append(number)
st.write('There are',len(evenlist),'even numbers')
st.write('There are',len(oddlist),'odd numbers')

