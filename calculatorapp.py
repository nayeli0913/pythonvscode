import streamlit as st 
from time import sleep

if 'screen_text' not in st.session_state:
    st.session_state['screen_text'] = ''

if 'eval_text' not in st.session_state:
    st.session_state['eval_text'] = ''

#Sst.write(st.session_state)

app1,app2,app3 = st.columns ([1,2,1])
with app2:
    
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    screen = st.text_input('',value=st.session_state['screen_text'],disabled=True)
    m1, m2, m3, m4 = st.columns(4)

    with m1:
        openb = st.button('(',use_container_width=True)
        if openb:
            st.session_state['screen_text'] += '('
            st.session_state['eval_text'] += '('
            st.rerun()

        seven = st.button('7',use_container_width=True)
        if seven:
            st.session_state['screen_text'] += '7'
            st.session_state['eval_text'] += '7'
            st.rerun()
        
        four = st.button('4',use_container_width=True)
        if four:
            st.session_state['screen_text'] += '4'
            st.session_state['eval_text'] += '4'
            st.rerun()
        
        one = st.button('1',use_container_width=True)
        if one:
            st.session_state['screen_text'] += '1'
            st.session_state['eval_text'] += '1'
            st.rerun()

        zero = st.button('0',use_container_width=True)
        if zero:
            st.session_state['screen_text'] += '0'
            st.session_state['eval_text'] += '0'
            st.rerun()

    with m2:
        closeb = st.button(')',use_container_width=True)
        if closeb:
            st.session_state['screen_text'] += ')'
            st.session_state['eval_text'] += ')'
            st.rerun()

        eight = st.button('8',use_container_width=True)
        if eight:
            st.session_state['screen_text'] += '8'
            st.session_state['eval_text'] += '8'
            st.rerun()

        five = st.button('5',use_container_width=True)
        if five:
            st.session_state['screen_text'] += '5'
            st.session_state['eval_text'] += '5'
            st.rerun()
            
        two = st.button('2',use_container_width=True)
        if two:
            st.session_state['screen_text'] += '2'
            st.session_state['eval_text'] += '2'
            st.rerun()
            
        point = st.button('.',use_container_width=True)
        if point:
            st.session_state['screen_text'] += '.'
            st.session_state['eval_text'] += '.'
            st.rerun()
            
    with m3:
        delete = st.button('DEL',use_container_width=True)
        if delete:
            del_value = st.session_state['screen_text']
            st.session_state ['screen_text'] = del_value[:-1]
            del_eval = st.session_state['eval_text']
            st.session_state['eval_text'] = del_eval[:-1]
            st.rerun()

        nine = st.button('9',use_container_width=True)
        if nine:
            st.session_state['screen_text'] += '9'
            st.session_state['eval_text'] += '9'
            st.rerun()
            
        six = st.button('6',use_container_width=True)
        if six:
            st.session_state['screen_text'] += '6'
            st.session_state['eval_text'] += '6'
            st.rerun()
            
        three = st.button('3',use_container_width=True)
        if three:
            st.session_state['screen_text'] += '3'
            st.session_state['eval_text'] += '3'
            st.rerun()
            
        plus = st.button('\+',use_container_width=True)
        if plus:
            st.session_state['screen_text'] += '+'
            st.session_state['eval_text'] += '+'
            st.rerun()
            
    with m4:
        clear = st.button('AC',use_container_width=True)
        if clear:
            st.session_state['screen_text'] = ''
            st.session_state['eval_text'] = ''
            st.rerun()

        division = st.button('÷',use_container_width=True)
        if division:
            st.session_state['screen_text'] += '÷'
            st.session_state['eval_text'] += '/'
            st.rerun()
            
        multiply = st.button('×',use_container_width=True)
        if multiply:
            st.session_state['screen_text'] += 'x'
            st.session_state['eval_text'] += '*'
            st.rerun()

        subtract = st.button('\-',use_container_width=True)
        if subtract:
            st.session_state['screen_text'] += '-'
            st.session_state['eval_text'] += '-'
            st.rerun()

        equals = st.button("=",use_container_width=True)
        if equals:
                try:
                    eval_result = eval(st.session_state['eval_text'])
                    st.session_state['eval_text'] = str(eval_result)
                    st.session_state['screen_text'] = str(eval_result)
                    st.rerun()
                except SyntaxError:
                    wrong = 'argument invalid'

    if equals:
        if st.session_state['eval_text'] != '':
            st.error(wrong)
            sleep(0.5)
            st.rerun()
        else:
            pass

