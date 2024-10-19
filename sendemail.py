import streamlit as st
from email.message import EmailMessage
#email configuration: sender, receiver, content/body, attachment
import ssl
#security
import smtplib
#send mail from sender to receiver

sender = 'githubtee@gmail.com'
password = 'cczaelfrzzyywngz'

receiver = st.text_input("Enter recepient's email")
subject = st.text_input('Enter email subject here')
body = st.text_area('Enter email content here',height=200)

if st.button('Send mail'):
    email = EmailMessage() #we want to create a new email
    email['From'] = sender
    email['To']= receiver
    email['subject'] = subject
    email.set_content(body)

    emailssl = ssl.create_default_context()#create a secure connection

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=emailssl) as smtp: #hostname, port, ssl
        #this helps us to connect to gmail server
        smtp.login(sender,password) #login to sender email
        smtp.sendmail(sender,receiver,email.as_string()) #send email as string to be readable
        st.success('Email successfully sent')
