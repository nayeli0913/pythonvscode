import streamlit as st

st.set_page_config(page_title='Videos site', page_icon='👓')
menu = st.sidebar.selectbox("Menu",['Videos','Video ratings'])

if menu == 'Videos':
    vidcat = st.sidebar.pills('Choose videos',['All','Baking','Music','Education','Animals'],default='All')

    if vidcat == 'All' or vidcat== 'Baking':
        st.subheader("Baking")

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.image("https://i.ytimg.com/vi/KmLgDi9FMeM/maxresdefault.jpg")
            st.write("Oreo cupcakes recipe")
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=KmLgDi9FMeM&t=46s&pp=ygUNb3JlbyBjdXBjYWtlcw%3D%3D')

        with c2:
            st.image("https://i.ytimg.com/vi/KvlAjbfv20M/maxresdefault.jpg")
            st.write("Red velvet cake recipe")
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=KvlAjbfv20M&pp=ygUPcmVkIHZlbHZldCBjYWtl')
            
        with c3:
            st.image("https://i.ytimg.com/vi/ji8qpeYWpgU/maxresdefault.jpg")
            st.write("Fudgy brownies recipe")
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=l5Z6oT6GAes&pp=ygUOZnVkZ3kgYnJvd25pZXM%3D')
        
        with c4:
            st.image("https://i.ytimg.com/vi/3orMJXkKk5o/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAIdlu8Ot-aXlJl9vfxE6-dUQ7KGQ")
            st.write("Sugar cookies recipe")
            st.link_button(label='Play Video',url='https://www.youtube.com/watch?v=txw2zaUW9UA&pp=ygUUc3VnYXIgY29va2llcyByZWNpcGU%3D')
    
    if vidcat == 'All' or vidcat == 'Music':
        st.subheader("Music")
        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.image("https://s.abcnews.com/images/Entertainment/240112_abcnl_prime_uchis1_hpMain_16x9_1600.jpg")
            st.write("Dead to me")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=OcUDK4kAUIw&pp=ygUKZGVhZCB0byBtZQ%3D%3D')
        with c2:
            st.image("https://i.ytimg.com/vi/o7fgFaXKVa0/maxresdefault.jpg")
            st.write("Duvet")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=o7fgFaXKVa0&ab_channel=B%C3%B4a-Topic')
        with c3:
            st.image("https://i.ytimg.com/vi/laDnsiKURTQ/maxresdefault.jpg")
            st.write("Apple cider")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=laDnsiKURTQ&ab_channel=Beabadoobee')
        with c4:
            st.image("https://i.ytimg.com/vi/6ztwSTu5B8A/maxresdefault.jpg")
            st.write("Mosquito")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=6ztwSTu5B8A')

    if vidcat == 'All' or vidcat == 'Education':

        st.subheader("Education")
        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.image("https://i.ytimg.com/vi/3tisOnOkwzo/maxresdefault.jpg")
            st.write("Biology explained")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=3tisOnOkwzo&pp=ygURYmlvbG9neSBleHBsYWluZWQ%3D')
        
        with c2:
            st.image("https://i.ytimg.com/vi/xuCn8ux2gbs/maxresdefault.jpg")
            st.write("History of the world")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=xuCn8ux2gbs&pp=ygUbaGlzdG9yeSBvZiB0aGUgZW50aXJlIHdvcmxk')

        with c3:
            st.image("https://i.ytimg.com/vi/3kE_Q-JdlO4/maxresdefault.jpg")
            st.write("Factorising quadratics")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=3kE_Q-JdlO4&pp=ygUWZmFjdG9yaXNpbmcgcXVhZHJhdGljcw%3D%3D')
        
        with c4:
            st.image("https://i.ytimg.com/vi/OtBqDgOsW1c/maxresdefault.jpg")
            st.write("Music theory")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=OtBqDgOsW1c&ab_channel=NoMad')
    
    if vidcat == 'All' or vidcat == 'Animals':

        st.subheader("Animals")
        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.image("https://i.ytimg.com/vi/lArqN_zu5tw/maxresdefault.jpg")
            st.write("Tortoise eating fruits")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=lArqN_zu5tw&pp=ygUUdHVydGxlIGVhdGluZyBncmFwZXM%3D')

        with c2:
            st.image("https://i.ytimg.com/vi/Zb3Wzs2FcFE/maxresdefault.jpg")
            st.write("Dog care guide")
            st.link_button(label='Play video',url='')
        
        with c3:
            st.image("https://i.ytimg.com/vi/xZS2kMKtBDs/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAubOlR89v5a2T2oLsN8VQSf7_0Gg")
            st.write("Cat cucumber prank")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=RBrZsgy4-SQ&pp=ygUMY2F0IGN1Y3VtYmVy')

        with c4: 
            st.image("https://i.ytimg.com/vi/KYnK5OuFdCE/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCq3k8D0s5BPS9eXgTHPsjC9n2MJg")
            st.write("Betta fish ecosystem")
            st.link_button(label='Play video',url='https://www.youtube.com/watch?v=KYnK5OuFdCE&pp=ygURYXF1YXJpdW0gYnVpbGRpbmc%3D')
