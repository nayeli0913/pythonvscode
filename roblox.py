"""
Daniel is thrilled to explore the Roblox store and enhance his gaming experience. 
He wants to purchase the game, select a game pass, buy some avatar outfits, and
 maybe even get a pet! Additionally, he’s considering buying some Robux to unlock 
 more features. Write a Python program to help Daniel calculate the total cost of his Roblox adventure.

Daniel’s journey through the Roblox store involves several steps:

First, he needs to purchase the game itself, which costs $150.
Daniel will then log in to his account using his username and password.
Next, he can choose between two game passes: the VIP pass for $50 or the Premium pass for $120.
Daniel can also browse through three different avatar outfits, each with its own price tag.
Additionally, Daniel has the option to add a pet to his gameplay for an additional $40.
Finally, he can purchase Robux: 800 Robux for $10, 2000 Robux for $25, or 4500 Robux for $50.
After making his selections, Daniel wants to see the total cost of his Roblox adventure. 

"""

import streamlit as st

totalcost = 150

u=st.text_input("enter username")
p=st.text_input("enter password")

pas=st.text_input("Type 1 to select the VIP pass for $50, Type 2 to select the premium pass for $120")

if pas == "1":
    totalcost+=50
elif pas == "2":
    totalcost+=120

av = st.text_input("type 1 for the $5 avatar, 2 for the $10 avatar, and 3 for the $15 avatar")

if av == "1":
    totalcost+=5
elif av == "2":
    totalcost+=10
elif av == "3":
    totalcost+=15

pet = st.text_input("Would you like to add a pet to your gameplay for $40?")

if pet == "yes":
    totalcost+=40

rob = st.text_input("Type 1 to buy 800 Robux for $10, 2 to by 2000 Robux for $25, or 3 to buy 4500 Robux for $50")

if rob == "1":
    totalcost+=10
elif rob == "2":
    totalcost+=25
elif rob == "3":
    totalcost+=50

if st.button("Check total"):
    print(totalcost)