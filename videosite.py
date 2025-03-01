import streamlit as st
import webbrowser
import pandas as pd

st.set_page_config(page_title='Videos site', page_icon='👓')
csvlink='videosrating.csv'

try:
    videocsv =pd.read_csv('videosrating.csv')
except:
    videocsv = pd.DataFrame()

st.table(videocsv)
menu = st.sidebar.selectbox("Menu",['Videos','Video ratings'])


if menu == 'Videos':
    vidcat = st.sidebar.pills('Choose videos',['All','Baking','Music','Education','Animals'],default='All')

    if vidcat == 'All' or vidcat== 'Baking':
        st.subheader("Baking")

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.image("https://i.ytimg.com/vi/KmLgDi9FMeM/maxresdefault.jpg")
            st.write("Oreo cupcakes recipe")
            if st.button('Play Video',key="1"):
                webbrowser.open("https://www.youtube.com/watch?v=KmLgDi9FMeM&t=46s&pp=ygUNb3JlbyBjdXBjYWtlcw%3D%3D")
                try:
                    videocsv.loc[0,'Oreo cupcakes recipe'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Oreo cupcakes recipe'] =1
                    videocsv.to_csv(csvlink,index=False)

        with c2:
            st.image("https://i.ytimg.com/vi/KvlAjbfv20M/maxresdefault.jpg")
            st.write("Red velvet cake recipe")
            if st.button('Play video',key="2"):
                webbrowser.open("https://www.youtube.com/watch?v=KvlAjbfv20M&pp=ygUPcmVkIHZlbHZldCBjYWtl")
                try:
                    videocsv.loc[0,'Red velvet cake recipe'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Red velvet cake recipe'] =1
                    videocsv.to_csv(csvlink,index=False)
        
        with c3:
            st.image("https://i.ytimg.com/vi/ji8qpeYWpgU/maxresdefault.jpg")
            st.write("Fudgy brownies recipe")
            if st.button('Play video',key="3"):
                webbrowser.open("https://www.youtube.com/watch?v=l5Z6oT6GAes&pp=ygUOZnVkZ3kgYnJvd25pZXM%3D")
                try:
                    videocsv.loc[0,'Fudgy brownies recipe'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Fudgy brownies recipe'] =1
                    videocsv.to_csv(csvlink,index=False)
        
        with c4:
            st.image("https://i.ytimg.com/vi/3orMJXkKk5o/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAIdlu8Ot-aXlJl9vfxE6-dUQ7KGQ")
            st.write("Sugar cookies recipe")
            if st.button('Play video',key="4"):
                webbrowser.open("https://www.youtube.com/watch?v=txw2zaUW9UA&pp=ygUUc3VnYXIgY29va2llcyByZWNpcGU%3D")
                try:
                    videocsv.loc[0,'Sugar cookies recipe'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Sugar cookies recipe'] =1
                    videocsv.to_csv(csvlink,index=False)
    
    if vidcat == 'All' or vidcat == 'Music':
        st.subheader("Music")
        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.image("https://i.ytimg.com/vi/ZKjIHQxG_3Q/maxresdefault.jpg")
            st.write("Sweet/Wanted to dance")
            if st.button('Play video',key="5"):
                webbrowser.open("https://www.youtube.com/watch?v=ZKjIHQxG_3Q")
                try:
                    videocsv.loc[0,'Sweet/Wanted to dance'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Sweet/Wanted to dance'] =1
                    videocsv.to_csv(csvlink,index=False)
    
        with c2:
            st.image("https://i.ytimg.com/vi/o7fgFaXKVa0/maxresdefault.jpg")
            st.write("Duvet")
            if st.button('Play video',key="6"):
                webbrowser.open("https://www.youtube.com/watch?v=o7fgFaXKVa0&ab_channel=B%C3%B4a-Topic")
                try:
                    videocsv.loc[0,'Duvet'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Duvet'] =1
                    videocsv.to_csv(csvlink,index=False)
    
        with c3:
            st.image("https://i.ytimg.com/vi/laDnsiKURTQ/maxresdefault.jpg")
            st.write("Apple cider")
            if st.button('Play video',key="7"):
                webbrowser.open("https://www.youtube.com/watch?v=laDnsiKURTQ&ab_channel=Beabadoobee")
                try:
                    videocsv.loc[0,'Apple cider'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Apple cider'] =1
                    videocsv.to_csv(csvlink,index=False)

        with c4:
            st.image("https://i.ytimg.com/vi/6ztwSTu5B8A/maxresdefault.jpg")
            st.write("Mosquito")
            if st.button('Play video',key="8"):
                webbrowser.open("https://www.youtube.com/watch?v=6ztwSTu5B8A")
                try:
                    videocsv.loc[0,'Mosquito'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Mosquito'] =1
                    videocsv.to_csv(csvlink,index=False)

    if vidcat == 'All' or vidcat == 'Education':

        st.subheader("Education")
        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.image("https://i.ytimg.com/vi/3tisOnOkwzo/maxresdefault.jpg")
            st.write("Biology explained")
            if st.button("Play video",key="9"):
                webbrowser.open("https://www.youtube.com/watch?v=3tisOnOkwzo&pp=ygURYmlvbG9neSBleHBsYWluZWQ%3D")
                try:
                    videocsv.loc[0,'Biology explained'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Biology explained'] =1
                    videocsv.to_csv(csvlink,index=False)
        
        with c2:
            st.image("https://i.ytimg.com/vi/xuCn8ux2gbs/maxresdefault.jpg")
            st.write("History of the world")
            if st.button("Play video",key="10"):
                webbrowser.open("https://www.youtube.com/watch?v=xuCn8ux2gbs&pp=ygUbaGlzdG9yeSBvZiB0aGUgZW50aXJlIHdvcmxk")
                try:
                    videocsv.loc[0,'History of the world'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'History of the world'] =1
                    videocsv.to_csv(csvlink,index=False)

        with c3:
            st.image("https://i.ytimg.com/vi/3kE_Q-JdlO4/maxresdefault.jpg")
            st.write("Factorising quadratics")
            if st.button("Play video",key="11"):
                webbrowser.open("https://www.youtube.com/watch?v=3kE_Q-JdlO4&pp=ygUWZmFjdG9yaXNpbmcgcXVhZHJhdGljcw%3D%3D")
                try:
                    videocsv.loc[0,'Factorising quadratics'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Factorising quadratics'] =1
                    videocsv.to_csv(csvlink,index=False)
        
        with c4:
            st.image("https://i.ytimg.com/vi/OtBqDgOsW1c/maxresdefault.jpg")
            st.write("Music theory")
            if st.button("Play video",key="12"):
                webbrowser.open("https://www.youtube.com/watch?v=OtBqDgOsW1c&ab_channel=NoMad")
                try:
                    videocsv.loc[0,'Music theory'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Music theory'] =1
                    videocsv.to_csv(csvlink,index=False)
    
    if vidcat == 'All' or vidcat == 'Animals':

        st.subheader("Animals")
        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.image("https://i.ytimg.com/vi/lArqN_zu5tw/maxresdefault.jpg")
            st.write("Tortoise eating fruits")
            if st.button("Play video",key="13"):
                webbrowser.open("https://www.youtube.com/watch?v=lArqN_zu5tw&pp=ygUUdHVydGxlIGVhdGluZyBncmFwZXM%3D")
                try:
                    videocsv.loc[0,'Tortoise eating fruits'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Tortoise eating fruits'] =1
                    videocsv.to_csv(csvlink,index=False)

        with c2:
            st.image("https://i.ytimg.com/vi/Zb3Wzs2FcFE/maxresdefault.jpg")
            st.write("Dog care guide")
            if st.button("Play video",key="14"):
                webbrowser.open("https://www.youtube.com/watch?v=peUVLEUj-AM&pp=ygUOZG9nIGNhcmUgZ3VpZGU%3D")
                try:
                    videocsv.loc[0,'Dog care guide'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Dog care guide'] =1
                    videocsv.to_csv(csvlink,index=False)
        
        with c3:
            st.image("https://i.ytimg.com/vi/xZS2kMKtBDs/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAubOlR89v5a2T2oLsN8VQSf7_0Gg")
            st.write("Cat cucumber prank")
            if st.button("Play video",key="15"):
                webbrowser.open("https://www.youtube.com/watch?v=RBrZsgy4-SQ&pp=ygUMY2F0IGN1Y3VtYmVy")
                try:
                    videocsv.loc[0,'Cat cucumber prank'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Cat cucumber prank'] =1
                    videocsv.to_csv(csvlink,index=False)

        with c4: 
            st.image("https://i.ytimg.com/vi/KYnK5OuFdCE/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCq3k8D0s5BPS9eXgTHPsjC9n2MJg")
            st.write("Betta fish ecosystem")
            if st.button("Play video",key="16"):
                webbrowser.open("https://www.youtube.com/watch?v=RBrZsgy4-SQ&pp=ygUMY2F0IGN1Y3VtYmVy")
                try:
                    videocsv.loc[0,'Betta fish ecosystem'] +=1
                    videocsv.to_csv(csvlink,index=False)
                except KeyError:
                    videocsv.loc[0,'Betta fish ecosystem'] =1
                    videocsv.to_csv(csvlink,index=False)
