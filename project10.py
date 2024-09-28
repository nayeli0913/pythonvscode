import streamlit as st

bill = 0

st.subheader("Calculate the total cost of going to the match.")


if st.checkbox("Purchase match ticket ($200)"):
    bill += 200
    st.text_input("Enter a username")
    st.text_input("Enter a password", type='password')
    if st.checkbox("Log in"):

        c1,c2 = st.columns(2)
        with c1:
            pas = st.radio("Select a season pass",['Standard ($200)','VIP ($500)'],horizontal=True)
            if pas == 'Standard ($200)':
                bill += 200
            elif pas == 'VIP ($500)':
                bill += 500
            merch = st.selectbox("Buy merchandise",['None','Jersey ($60)','Scarf ($30)','Hat ($20)'])
            if merch == 'Jersey ($60)':
                bill += 60
            elif merch == 'Scarf ($30)':
                bill += 30
            elif merch == 'Hat ($20)':
                bill += 20
        with c2:
            snac = st.selectbox("Buy snacks",['None',"Popcorn ($10)",'Hotdog ($15)','Soda ($5)'])
            if snac == "Popcorn ($10)":
                bill += 10
            elif snac == 'Hotdog ($15)':
                bill += 15
            elif snac == 'Soda ($5)':
                bill += 5
            sub = st.selectbox("Premium sports channel subscription",['None','Monthly ($20)','Annual ($10)'])
            if sub == 'Monthly ($20)':
                bill+= 20
            elif sub == 'Annual ($10)':
                bill += 10
            
        if st.button ("Calculate final price"):
            st.subheader(bill)