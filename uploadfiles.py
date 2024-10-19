import streamlit as st
import pandas as pd
import plotly.express as px

menu = st.sidebar.selectbox('Choose an option',['Upload CSV','Upload image','Upload audio','Upload video'])

if menu == 'Upload CSV':
    st.subheader("Upload and view CSV database")
    uploadcsv = st.file_uploader('Upload your CSV file here',type='csv')

    if uploadcsv:
        readcsv = pd.read_csv(uploadcsv)

        with st.expander("View CSV Table"):
            st.table(readcsv)
        

        readcsvcolumns = readcsv.columns #read all columns in csv
        selectcolumns = st.multiselect('Choose columns to plot',readcsvcolumns)
        
        column = readcsv[selectcolumns].mean().reset_index()
        barchart= px.bar(column,x='index', y=0)
        st.plotly_chart(barchart)

if menu == 'Upload image':
    st.subheader("Upload and view image ")
    uploadimg = st.file_uploader('Upload your image here',type=['png','jpg','jpeg','webp'])

    if uploadimg:
        st.image(uploadimg)

if menu == 'Upload audio':
    st.subheader("Upload and listen to audio")
    uploadaud = st.file_uploader('Upload your audio here',type=['mp3','wav'])

    if uploadaud:
        st.audio(uploadaud,format='audio/mp3')

if menu == 'Upload video':
    st.subheader("Upload and watch video")
    youtubelink = st.text_input('Paste in your youtube video link')

    if youtubelink:
        if st.button("Play youtube video"):
            try:
                st.video(youtubelink)
            except:
                st.error('Please enter a valid youtube link')