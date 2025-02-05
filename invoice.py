import streamlit as st
from fpdf import FPDF 
import base64 #python module to convert binary data (of the code) to printable character

menu = st.sidebar.selectbox('Menu',['Invoice generator','Change details'])
tax = st.sidebar.number_input('Enter tax %')
discount = st.sidebar.number_input('Enter discount %')
logo = 'crum.png'


if menu == 'Invoice generator':
    c1,c2 = st.columns(2)
    with c1:
        st.image(logo,width=50)
        st.write('Crumbl Cookies')
        st.write('The Fairfax, 1195 3rd Ave')
        st.write('New York, NY 10021, United States')
    with c2:
        st.subheader('INVOICE')
    c3,c4 = st.columns(2)
    with c3:
        bname = st.text_input('Bill to:',placeholder='Customer Name')
        email = st.text_input('em',label_visibility='collapsed',placeholder='Customer email')
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

def generatepdf():
    pdf = FPDF()


    #Add a new page
    pdf.add_page()

    xpos = 20
    ypos = 30
    colw = 90

    #add logo
    pdf.image(logo,x=xpos,y=ypos,w=50)

    #invoice
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+125,ypos+25)
    pdf.cell(w=colw,txt='INVOICE',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+40)
    pdf.cell(w=colw,txt='Crumbl cookies',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+50)
    pdf.cell(w=colw,txt='The Fairfax, 1195 3rd Ave',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+60)
    pdf.cell(w=colw,txt='New york, NY 10021, United States',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+90)
    pdf.cell(w=colw,txt='BILL TO:',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+100)
    pdf.cell(w=colw,txt=f'{bname}',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+110)
    pdf.cell(w=colw,txt=f'{email}',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+110,ypos+100)
    pdf.cell(w=colw,txt=f'Invoice #: {invnum}',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+110,ypos+110)
    pdf.cell(w=colw,txt=f'Invoice Date: {invdate}',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+140)
    pdf.cell(w=colw,txt=f'DESCRIPTION',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+85,ypos+140)
    pdf.cell(w=colw,txt=f'Quantity',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+110,ypos+140)
    pdf.cell(w=colw,txt=f'Price|Unit',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+140,ypos+140)
    pdf.cell(w=colw,txt=f'Total price',ln=True)

    #line
    pdf.set_line_width(0.5)
    pdf.line(xpos,ypos+145,xpos+175,ypos+145)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+150)
    pdf.cell(w=colw,txt=f'{desc}',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+85,ypos+150)
    pdf.cell(w=colw,txt=f'{quant}',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+85,ypos+160)
    pdf.cell(w=colw,txt=f'Tax:${taxcalc}',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+110,ypos+150)
    pdf.cell(w=colw,txt=f'${price}',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+110,ypos+160)
    pdf.cell(w=colw,txt=f'Discount:${discountcalc:,}',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos+140,ypos+150)
    pdf.cell(w=colw,txt=f'${total:,}',ln=True)


    pdf.set_font(family='Courier',size=16,style='B')
    pdf.set_xy(xpos,ypos+190)
    pdf.cell(w=colw,txt=f'PAYMENT INFORMATION',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+200)
    pdf.cell(w=colw,txt=f'Acc name: Crumbl Cookies',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+205)
    pdf.cell(w=colw,txt=f'Acc number: 0976896263',ln=True)

    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(xpos,ypos+210)
    pdf.cell(w=colw,txt=f'Bank name: Td Canada',ln=True)

    pdf.set_font(family='Courier',size=16,style='B')
    pdf.set_xy(xpos+110,ypos+190)
    pdf.cell(w=colw,txt=f'PAYMENT DUE',ln=True)

    pdf.set_font(family='Courier',size=32,style='B')
    pdf.set_xy(xpos+110,ypos+205)
    pdf.cell(w=colw,txt=f'${finaltotal:,}',ln=True)

    #save the PDF
    pdf_file = 'invoice.pdf'
    pdf.output('invoice.pdf')
    return pdf_file


callpdf = generatepdf() #calls function
with open(callpdf,'rb') as genpdf: #opens generator function
    readpdf = genpdf.read() #reads generator function

#if st.button("View Invoice"):
#    if '@' in email :
#        st.success('correct')
#        if bname and email and invdate and invnum and duedate and desc and quant and price:

#            write_pdf = base64.b64encode(readpdf).decode('utf-8')
#            embed_pdf = f'<embed src="data:application/pdf;base64, {write_pdf}" type="application/pdf" width="70%" height="600px" />'
#            st.markdown (embed_pdf, unsafe_allow_html=True)

if '@' in email :
    if bname and email and invdate and invnum and duedate and desc and quant and price:

        st.download_button(label='Download Invoice',data=readpdf,file_name="CrumblInvoice.pdf",mime='application/pdf')
    else:
            st.error("All boxes need to be filled")
else:
        st.error("Invalid email")