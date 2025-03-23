import streamlit as st
import pandas as pd

#Dropdown 1 - sidebar 
selectbox1= st.sidebar.selectbox('Choose an option from the menu below', ['Home', 'About us'])

if selectbox1=='Home':
    selectbox2= st.sidebar.selectbox('Choose an option from the menu below', ['Live Sessions', 'Recordings', 'Homework Materials', 'Other Resources'])
    button_sb= st.sidebar.button('Contact us')

    #Promt user to login or create an account
    home_col1, home_col2 = st.columns(2)
    with home_col1:
        login= st.button('Login')
    with home_col2:
        createacc= st.button('Create Account')

    st.title('Welcome to Axle!')
    st.write('Accessible learning for all')

    if selectbox2=='Live Sessions':
        st.title('Live Sessions')
        st.write('Please use the slider below to select the time in your current location:')
        slider= st.slider('Select:', min_value=1, max_value=24, value=12, step=1)
        if slider<12:
            st.write(f'You selected ', {slider}, 'a.m.')
        else:
            st.write(f'You selected ', {slider}, 'p.m.')
        
        if slider==5 or slider==12 or slider==21:
            st.header('Available Sessions:')
            ls_col1, ls_col2 = st.columns(2)
            if slider ==5:
                with ls_col1:
                    st.write('Example 1. subject- lesson #- teacher- 5:00pm')
                    st.write('Example 2. subject- lesson #- teacher- 5:30pm')
                    st.write('Example 3. subject- lesson #- teacher- 6:00pm')  
                with ls_col2:
                    st.write()
                    st.button("Join", key=1)
                    st.button("Join", key=2)
                    st.button("Join", key=3)
            elif slider ==12:
                with ls_col1:
                    st.write('Example 1. subject- lesson #- teacher- 12:15pm')
                    st.write('Example 2. subject- lesson #- teacher- 12:45pm')
                    st.write('Example 3. subject- lesson #- teacher- 13:00pm')
                with ls_col2:
                    st.write()               
                    st.button("Join", key=1)
                    st.button("Join", key=2)
                    st.button("Join", key=3)
            elif slider==21:
                with ls_col1:
                    st.write('Example 1. subject- lesson #- teacher- 21:15pm')
                    st.write('Example 2. subject- lesson #- teacher- 21:30pm')
                    st.write('Example 3. subject- lesson #- teacher- 21:45pm')
                    st.write('Example 4. subject- lesson #- teacher- 22:00pm')
                with ls_col2:
                    st.write()
                    st.button("\n\nJoin", key=1)
                    st.button("Join", key=2)
                    st.button("Join", key=3)
                    st.button("Join", key=4)
        else:
            st.header('Sorry, there are no available live sessions at this time.')


    elif selectbox2=='Recordings':
        st.title('Recordings')
        st.write('Below, you have free access to recordings from live sessions and from other teachers!')

    elif selectbox2=='Homework Materials':
        st.title('Homework Materials')
    else: 
        st.title('Other Resources')

else: 
    button_sb= st.sidebar.button('Contact us')
    st.title('About us')
    st.write()
    

    

