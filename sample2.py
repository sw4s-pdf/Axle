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
