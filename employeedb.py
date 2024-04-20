import streamlit as st

import pandas as pd
st.set_page_config(layout='wide')
df = pd.read_csv('employee.csv')
user_id= "USER" + str(len(df) +1)

menu = st.sidebar.selectbox('Menu',['Register here','Employee file', 'Database'])

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

      findbutton = st.button('Find employee')

    if findbutton:
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

          else:
             st.error("Employee ID not found")

if menu =='Database':
    st.dataframe(df,use_container_width=True)