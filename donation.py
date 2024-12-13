import streamlit as st
import pandas as pd
import plotly.express as px

menu = st.sidebar.selectbox('Menu',['Create donation campaign','View donations','Donate'])

df = pd.read_csv('donate.csv')
try:
    dfadd = pd.read_csv('donateadd.csv')
except pd.errors.EmptyDataError:
    dfadd = pd.DataFrame()

if menu == 'Create donation campaign':
    st.subheader(":red[Create donation]")

    c1,c2 = st.columns(2)
    with c1:
        campaign = st.text_input("Campaign title")
    with c2:
        email = st.text_input("Email")

    details = st.text_area('Campaign details',height=200)
    goal = st.selectbox('Goal amount',['$50','$100','$200','$500','custom'],)
    if goal == '$50':
        goal = 50
    if goal == '$100':
        goal = 100
    if goal == '$200':
        goal = 200
    if goal == '$500':
        goal = 500
    if goal == 'custom':
        goal = st.number_input('Enter custom goal amount')
    
    createcam = st.button('create campaign')

    if createcam:
        donatedict = {"Campaign title":[campaign],"Email":[email],"Campaign details":[details],"Goal":[goal]}
        donatedf = pd.DataFrame(donatedict)
        newdf = pd.concat([df,donatedf])
        newdf.to_csv('donate.csv',index=False)

    if createcam:
        if campaign not in dfadd.columns:
            dfadd[campaign]= ''
        dfadd.to_csv('donateaddcsv')
        st.success('Campaign submitted')

if menu == 'View donations':
    st.subheader(':red[View donations]')
    titles = df['Campaign title']
    cl1,cl2 = st.columns(2)
    with cl1:
        choosetitle = st.selectbox("Select donation campaign to view",titles)
        filter = df[df['Campaign title'] == choosetitle]
        getdetails= filter['Campaign details'].iloc[0]
        getgoal = filter['Goal'].iloc[0]
        getemail = filter['Email'].iloc[0]

        try:
            getcontrib = dfadd[choosetitle].sum()
        except KeyError:
                st.error("no contributions yet")

    col1,col2,col3 = st.columns(3)
    st.divider()
    with col1:
        st.subheader("Campaign details")
    with col2:
        st.subheader(f":red[Goal ammount: ${getgoal}]")
    with col3:
        gl = float(getgoal) - getcontrib
        if gl <= 0:
            st.subheader('Goal completed')
        else:
            st.subheader(f":red[Goal left: ${gl}]")

    st.write(getdetails)
    st.write(f":red[Contact at : {getemail}]")

if menu == 'Donate':
    st.subheader(':red[Make a donation]')
    st.table(dfadd)
    titles = df['Campaign title']
    colm1, colm2 = st.columns(2)
    with colm1:
        selecttitles = st.selectbox('Select donation campaign',titles)
        donate = st.number_input('Enter donation ammount',0,step=500)
        if st.button('Donate'):
            if donate:
                donateadddict={f'{selecttitles}':[donate]}
                donateaddtable = pd.DataFrame(donateadddict)
                donateaddjoin = pd.concat([dfadd,donateaddtable],ignore_index=True)
                donateaddjoin.to_csv('donateadd.csv',index=False)
                st.success('Thank you for your donation!')
            else:
                st.error('Enter a valid donation')
