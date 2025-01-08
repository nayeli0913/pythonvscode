import streamlit as st

menu = st.sidebar.selectbox('Menu',['Invoice generator','Change details'])
tax = st.sidebar.number_input('Enter tax %')
discount = st.sidebar.number_input('Enter discount %')

if menu == 'Invoice generator':
    c1,c2 = st.columns(2)
    with c1:
        st.image('https://www.shopsatriverwalk.com/wp-content/uploads/2020/09/crumbl-cookies.jpg',width=50)
        st.write('Crumbl Cookies')
        st.write('The Fairfax, 1195 3rd Ave')
        st.write('New York, NY 10021, United States')
    with c2:
        st.subheader('INVOICE')
    c3,c4 = st.columns(2)
    with c3:
        bname = st.text_input('Bill to:')
        email = st.text_input('em',label_visibility='collapsed')
    with c4:
        cl1,cl2 = st.columns(2)
        with cl1:
            st.write('')
            st.write('Invoice#:')
            st.write('')
            st.write('Invoice date:')
            st.write('Due date:')
        with cl2:
            invnum = st.text_input('inv',label_visibility='collapsed')
            invdate = st.date_input('invd',label_visibility='collapsed')
            duedate = st.date_input('due',label_visibility='collapsed')
    st.write('')
    c5,c6,c7,c8 = st.columns(4)
    with c5:
        desc = st.text_input('Description:')
    with c6:
        quant = st.number_input('Quantity:')
    with c7:
        price = st.number_input('Price|unit:')
        total = quant * price
        taxcalc = tax/100 * total
        st.write(f"Tax: ${taxcalc}")
    with c8:
        tprice = st.text_input("Total price", placeholder=f'${total:,}', disabled=True)
        discountcalc = discount/100 * total
        st.write(f"Discount: ${discountcalc}")
    st.divider()
    a1,a2 = st.columns(2)
    with a1:
        st.write("Payment info:")
        st.write("Acc name: Crumbl Cookies")
        st.write("Acc number: 0976896263")
        st.write("Bank name: Td Canada")
    with a2:
        st.write("Payment due:")
        finaltotal = total + taxcalc - discountcalc
        st.title(f"${finaltotal:,}")