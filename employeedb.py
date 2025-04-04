import streamlit as st
from fpdf import FPDF 
import pandas as pd
st.set_page_config(layout='wide')
df = pd.read_csv('employee.csv')
user_id= "USER" + str(len(df) +1)

menu = st.sidebar.selectbox('Menu',['Register here', 'Database', 'Employee file'])

if menu =='Register here':

   st.subheader('Register your employee')
   r1,r2 = st.columns(2)

   with r1:
      fn = st.text_input('Enter first name')
      email = st.text_input('Enter email')
      education = st.selectbox('Education level',['College','Masters degree','Bachelors degree','Post-graduate'])
      dep = st.selectbox('Department',['Sales','Engineering','Marketing','Management'])
      empdate = st.date_input('Employment date')
#intern junior senior supervisor manager 
   with r2:
      ln = st.text_input('Enter last name')
      gender = st.radio('Select gender',['Male','Female'],horizontal=True)
      st.write('')
      salary = st.number_input('Monthly salary')
      title = st.selectbox('Job title',['Intern','Junior','Senior','Supervisor','Manager'])
      status = st.selectbox('Employee status',['Part time','Full time'])
   
   date = st.date_input('Enter the registration date')

   if st.button('Submit'):
      employee_df = pd.DataFrame({"User ID":[user_id],"First name":[fn],"Last name":[ln],"Email":[email],"Gender":[gender],
                                    "Education":[education],"Salary":[salary],"Department":[dep],"Job title":[title],
                                    "Employment date":[empdate],"Employee status":[status]})
      new_df = pd.concat([df,employee_df])
      new_df.to_csv('employee.csv',index=False)
      st.success("Employee registered")


if menu == 'Employee file':
   t1,t2,t3 = st.columns(3)
   with t3:
      st.subheader('Find an employee here')
      st.write('')
      employee = st.text_input('Enter employee ID')

      findbutton = st.checkbox('Show employee info')

   if findbutton == True:
      if employee:
         findresult = df[df['User ID'] == employee]
         #st.dataframe(findresult)

         if not findresult.empty:
            getid = findresult['User ID'].iloc[0]
            getfn = findresult['First name'].iloc[0]
            getln = findresult['Last name'].iloc[0]
            getem = findresult['Email'].iloc[0]
            getgn = findresult['Gender'].iloc[0]
            geted = findresult['Education'].iloc[0]
            getsa = findresult['Salary'].iloc[0]
            getdp = findresult['Department'].iloc[0]
            getjt = findresult['Job title'].iloc[0]
            getep = findresult['Employment date'].iloc[0]
            getes = findresult['Employee status'].iloc[0]

            st.subheader(f':green[{getfn} {getln}]')
            st.write('')
            st.write('')
            st.subheader('Personal information')
            st.divider()

            c1,c2,c3 = st.columns(3)

            with c1: 
               st.write('Email')
               st.write(getem)
            with c2:
               st.write('Gender')
               st.write(getgn)
            with c3:
               st.write('Education level')
               st.write(geted)

            st.divider()
            st.subheader('Job information')
            st.divider()

            a1,a2,a3 = st.columns(3)

            with a1:
               st.write('Department')
               st.write(getdp)
            with a2:
               st.write('Employee ID')
               st.write(getid)
            with a3:
               st.write('Date of employment')
               st.write(getep)
            
            st.divider()

            b1,b2,b3 = st.columns(3)

            with b1:
               st.write('Job title')
               st.write(getjt)
            with b2:
               st.write('Employee status')
               st.write(getes)
            with b3:
               st.write('Salary')
               st.write(f"{getsa}")
            
            st.divider()

            def generatepdf():
               pdf = FPDF()

               pdf.add_page()

               xpos = 20
               ypos = 30
               colw = 90

               pdf.set_font(family='Courier',size=30,style='B')
               pdf.set_xy(xpos,ypos+70)
               pdf.cell(w=colw,txt=f'{getfn} {getln}',ln=True)

               pdf.set_line_width(0.5)
               pdf.line(xpos,ypos+75,xpos+145,ypos+75)

               pdf.set_font(family='Courier',size=12,style='B')
               pdf.set_xy(xpos,ypos+85)
               pdf.cell(w=colw,txt=f'Email',ln=True)
               pdf.set_font(family='Courier',size=12)
               pdf.set_xy(xpos,ypos+90)
               pdf.cell(w=colw,txt=f'{getem}',ln=True)

               pdf.set_font(family='Courier',size=12,style='B')
               pdf.set_xy(xpos+50,ypos+85)
               pdf.cell(w=colw,txt=f'Gender',ln=True)
               pdf.set_font(family='Courier',size=12)
               pdf.set_xy(xpos+50,ypos+90)
               pdf.cell(w=colw,txt=f'{getgn}',ln=True)

               pdf.set_font(family='Courier',size=12,style='B')
               pdf.set_xy(xpos+100,ypos+85)
               pdf.cell(w=colw,txt=f'Education',ln=True)
               pdf.set_font(family='Courier',size=12)
               pdf.set_xy(xpos+100,ypos+90)
               pdf.cell(w=colw,txt=f'{geted}',ln=True)

               pdf.set_font(family='Courier',size=12,style='B')
               pdf.set_xy(xpos,ypos+100)
               pdf.cell(w=colw,txt=f'Salary',ln=True)
               pdf.set_font(family='Courier',size=12)
               pdf.set_xy(xpos,ypos+105)
               pdf.cell(w=colw,txt=f'${getsa:,}',ln=True)

               pdf.set_font(family='Courier',size=12,style='B')
               pdf.set_xy(xpos+50,ypos+100)
               pdf.cell(w=colw,txt=f'Department',ln=True)
               pdf.set_font(family='Courier',size=12)
               pdf.set_xy(xpos+50,ypos+105)
               pdf.cell(w=colw,txt=f'{getdp}',ln=True)

               pdf.set_font(family='Courier',size=12,style='B')
               pdf.set_xy(xpos+100,ypos+100)
               pdf.cell(w=colw,txt=f'Job Title',ln=True)
               pdf.set_font(family='Courier',size=12)
               pdf.set_xy(xpos+100,ypos+105)
               pdf.cell(w=colw,txt=f'{getjt}',ln=True)

               pdf.set_font(family='Courier',size=12,style='B')
               pdf.set_xy(xpos,ypos+115)
               pdf.cell(w=colw,txt=f'Employee status',ln=True)
               pdf.set_font(family='Courier',size=12)
               pdf.set_xy(xpos,ypos+120)
               pdf.cell(w=colw,txt=f'{getes}',ln=True)

               pdf.set_font(family='Courier',size=12,style='B')
               pdf.set_xy(xpos+100,ypos+115)
               pdf.cell(w=colw,txt=f'Employment date',ln=True)
               pdf.set_font(family='Courier',size=12)
               pdf.set_xy(xpos+100,ypos+120)
               pdf.cell(w=colw,txt=f'{getep}',ln=True)
               
               pdf_file = 'employeeinfo.pdf'
               pdf.output('employeeinfo.pdf')
               return pdf_file
            
            callpdf = generatepdf() 
            with open(callpdf,'rb') as genpdf: 
               readpdf = genpdf.read()
            
            st.sidebar.download_button(label='Download employee file',data=readpdf,file_name="employeeinfo.pdf")
            

         else:
            st.error("Employee ID not found")

if menu =='Database':
   st.dataframe(df,use_container_width=True)