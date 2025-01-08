#Make an app that can upload a csv file, 
#asks users to choose columns to plot (use multiselectbox) hint to get columns is readcsvfile.columns
#choose what type of chart to plot
#then plot what the users selected

import streamlit as st
import pandas as pd
import plotly.express as px

upload = st.file_uploader('Upload a CSV file here',type='csv')

if upload:
    readcsv = pd.read_csv(upload)
    
    readcol = readcsv.columns
    selectcol = st.multiselect('Choose columns to plot',readcol)

    if selectcol:
        graph = st.selectbox('Type',['barchart','piechart'])

        if graph == 'barchart':
            column = readcsv[selectcol].mean().reset_index()
            barchart = px.bar(column, x='index',y=0,labels={'index':' ','0':' '})
            st.plotly_chart(barchart)
        elif graph == 'piechart':
            column = readcsv[selectcol].mean().reset_index()
            piechart = px.pie(column,names='index', values=0)
            st.plotly_chart(piechart)