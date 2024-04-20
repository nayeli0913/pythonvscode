# create a restaurant app
# -Add a restaurant picture
# -Create a restaurant app that welcomes users and shows them the food selections
# -If they choose/select their meals, show them the total amount
# -Ask a question if you want to share the bill with others #use checkbox
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill

import streamlit as st

st.set_page_config(layout = 'wide')

bill = 0

st.title("Ricebowl restaurant")

st.image('https://media.istockphoto.com/id/611611888/zh/%E7%85%A7%E7%89%87/rice.jpg?s=612x612&w=0&k=20&c=sOe789khc6IOk-ZC0exBvNRc4NQtX3nfNlqfEe7WSYM=')

st.subheader("Rice")

r1,r2,r3 = st.columns(3)

with r1:
    if st.checkbox('plain'):
     bill+=10
     st.success("Added to bowl")

with r2:
   if st.checkbox('fried'):
     bill+=20
     st.success("Added to bowl")

with r3:
   if st.checkbox('golden'):
     bill+=30
     st.success("Added to bowl")

st.subheader('sauce')

s1,s2,s3 = st.columns(3)

with s1:
   if st.checkbox('soy sauce'):
      bill+=10
      st.success("added to bowl")
   if st.checkbox('mayonnaise'):
      bill+=5
      st.success("added to bowl")

with s2:
   if st.checkbox('ketchup'):
      bill+=5
      st.success("added to bowl")
   if st.checkbox('sesame sauce'):
      bill+=10
      st.success("added to bowl")

with s3:
   if st.checkbox('curry'):
      bill+=10
      st.success("added to bowl")

st.subheader('toppings')
t1,t2,t3,t4= st.columns(4)

with t1:
   if st.checkbox('egg'):
      bill+=10
      st.success("added to bowl")
   if st.checkbox('chicken'):
      bill+=10
      st.success("added to bowl")

with t2:
   if st.checkbox('spring onion'):
      bill+=10
      st.success("added to bowl")
   if st.checkbox('pork'):
      bill+=10
      st.success("added to bowl")

with t3:
   if st.checkbox('veggies'):
      bill+=10
      st.success("added to bowl")
   if st.checkbox('ham'):
      bill+=10
      st.success("added to bowl")

with t4:
   if st.checkbox('Salt'):
      bill+=10
      st.success("added to bowl")
   if st.checkbox('pepper'):
      bill+=10
      st.success("added to bowl")

st.subheader('Drinks')

d1,d2,d3,d4= st.columns(4)

with d1:
   if st.checkbox('Water'):
      bill+=5
      st.success("Added to meal")
   if st.checkbox('Lemonade'):
      bill+=5
      st.success("Added to meal")
with d2:
   if st.checkbox('Orange juice'):
      bill+=5
      st.success("Added to meal")
   if st.checkbox('Apple juice'):
      bill+=5
      st.success("Added to meal")
with d3:
   if st.checkbox('Milk tea'):
      bill+=5
      st.success("Added to meal")
   if st.checkbox('Tea'):
      bill+=5
      st.success("Added to meal")
with d4:
   if st.checkbox('Coffee'):
      bill+=5
      st.success("Added to meal")

if st.button("check price"):
   st.subheader(f"Your total cost is ${bill}")

if st.checkbox('click to share bill with others'):
   people = st.slider('How many people in total?',2,50)
   person = bill/people
   st.subheader(f"Each person will pay ${person}")