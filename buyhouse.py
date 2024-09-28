# write a python program for house buyers
# create a menu for the buy house page and the house database page
# Ask them for their name
# ask them for their yearly salary
# if they earn below 100000 they can buy or rent an apartment
# If the earn between 100000-500,000 they can buy a bungalow
# If the earn between >500,000-1,000,000 they can buy a duplex
# If the earn between >1,000,000-5,000,000 they can buy a manshion
# if the earn above 5000000 they can buy an estate
# create a database to to store and view their answers and display in another customer section

import streamlit as st

import pandas as pd
df = pd.read_csv('house.csv')

menu = st.sidebar.selectbox('Menu',["Buy house", 'Database'])

if menu == 'Buy house':
    name = st.text_input("Enter your name")
    ys = st.number_input("Enter yearly salary")

    if st.button("Submit"):

      if ys <= 100000:
        house = ("Apartment")
      elif ys <= 500000:
        house = ("Bungalow")
      elif ys <= 1000000:
        house = ("Duplex")
      elif ys <= 5000000:
        house = ("Mansion")
      elif ys > 5000000:
        house = ("Estate")

      house_df = pd.DataFrame({"Resident name":[name],"Yearly salary":[ys],"Eligible house":[house]})
      new_df = pd.concat([df,house_df])
      new_df.to_csv('house.csv',index=False)
      st.success("Employee registered")

if menu == 'Database':
  st.dataframe(df,use_container_width=True)