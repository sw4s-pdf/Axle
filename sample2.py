import streamlit as st

# Create a selectbox for "screen navigation"
screen = st.sidebar.selectbox("Choose a screen", ["Main", "New Screen"])

# Main screen content
if screen == "Main":
    st.title("Main Screen")
    st.button("Go to New Screen")  # Just a button to simulate action

# New screen content
elif screen == "New Screen":
    st.title("New Screen")
    st.write("You are now on a new screen!")
    content = "This is a sample text file."

import streamlit as st

# Content to be downloaded
content = "This is a sample text file."

# Create a download button for the text file
st.download_button(
    label="Download Text File",
    data=content,
    file_name="sample.pdf",
    mime="txt/pdf"
)
