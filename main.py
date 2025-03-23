import streamlit as st
import pandas as pd

#Dropdown 1 - sidebar 
selectbox1= st.sidebar.selectbox('Choose an option from the menu below', ['Home', 'Ask Axle Bot','About us'])

if selectbox1=='Home':
    selectbox2= st.sidebar.selectbox('Choose an option from the menu below', ['Select...', 'Live Sessions', 'Recordings', 'Homework Materials', 'Other Resources',])
    button_sb= st.sidebar.button('Contact us')

    if button_sb:
        st.sidebar.title('Contact us')
        st.sidebar.write('Have any questions? Feel free to contact us using any of the methods below! ')
        st.sidebar.header('📞: 403-XXX-XXXX')
        st.sidebar.header('📤: axle.edu@xxxx.com')
        st.sidebar.header('Office Hours')
        st.sidebar.write('Mon-Fri : 8a.m - 4p.m')
        st.sidebar.write('Sat : 8a.m - 2p.m')
        st.sidebar.write('Sun : CLOSED')

    #Promt user to login or create an account
    home_col1, home_col2 = st.columns(2)
    with home_col1:
        login= st.button('Login')
    with home_col2:
        createacc= st.button('Create Account')

    st.title('Welcome to Axle!')
    st.write('Accessible learning for all')

    st.markdown('---')

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
        st.video('https://youtu.be/xvFZjo5PgG0?si=Sqnyv1MNBg54ecsJ')
        st.video('https://youtu.be/MtN1YnoL46Q?si=Fvc9xEo8A4ZqsEVT')

    elif selectbox2=='Homework Materials':
        st.title('Homework Materials')
        ex1= "Example 1"
        st.download_button(
            label= 'Download pdf',
            data= ex1, 
            file_name= 'example1.pdf',
            mime= 'txt/pdf'
        )
        ex2= 'Example 2'
        st.download_button(
            label= 'Download pdf',
            data= ex1, 
            file_name= 'example2.pdf',
            mime= 'txt/pdf'
        )
        ex3= 'Example 3'
        st.download_button(
            label= 'Download pdf',
            data= ex3, 
            file_name= 'example3.pdf',
            mime= 'txt/pdf'
        )
    elif selectbox2== 'Other Resources': 
        st.title('Other Resources')
        st.header('Youtube Videos:')
        st.markdown('Example 1- https://www.youtube.com')
        st.markdown('Example 2- https://www.youtube.com')
        st.markdown('Example 3- https://www.youtube.com')
        st.header('Websites:')
        st.markdown('Example 1- https://www.google.com')
        st.markdown('Example 2- https://www.google.com')
        st.markdown('Example 3- https://www.google.com')

elif selectbox1== 'Ask Axle Bot':
    st.title("Axle Bot")
    with st.chat_message('user'):
        st.write('Hello, I am Axle! What can I help you with today?')
    user_msg = st.chat_input(
    "Type your question here and/or attatch an image...",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
    )
    if user_msg and user_msg.text:
        st.markdown(user_msg.text)
    if user_msg and user_msg["files"]:
        st.image(user_msg["files"][0])             
elif selectbox1== 'About us': 
    button_sb= st.sidebar.button('Contact us')
    st.title('About us')
    st.write()

    if button_sb:
        st.sidebar.title('Contact us')
        st.sidebar.write('Have any questions? Feel free to contact us using any of the methods below! ')
        st.sidebar.header('📞: 403-XXX-XXXX')
        st.sidebar.header('📤: axle.edu@xxxx.com')
        st.sidebar.header('Office Hours')
        st.sidebar.write('Mon-Fri : 8a.m - 4p.m')
        st.sidebar.write('Sat : 8a.m - 2p.m')
        st.sidebar.write('Sun : CLOSED')