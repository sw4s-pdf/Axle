import streamlit as st

# Title and description for the website-like page
st.title("My Webebebsite-Like Page")
st.write("Welcome to my personal Streamlit app. Here, I'll show you how to create a webpage-like structure using Streamlit.")

# Sidebar for navigation or additional content
st.sidebar.header("Navigation")
st.sidebar.write("Use this sidebar to navigate through sections.")
st.sidebar.button("Click Me")

# Add some sections to simulate a multi-page experience
st.header("About Me")
st.write("Hello, I am a data enthusiast who loves building interactive applications using Python and Streamlit.")

# Add a sample image to the website
st.header("My Favorite Image")
st.image("https://via.placeholder.com/600x400.png?text=Sample+Image", caption="An example image", use_column_width=True)

# Show a button that triggers an action
if st.button('Click Me', key='button1'):
    st.write("You clicked the button!")

# Add some interactivity using a slider
st.header("Interactive Slider")
slider_value = st.slider("Select a number", 0, 100, 25, key='slider 1')
st.write(f"You selected {slider_value}")

col1, col2 = st.columns(2)

with col1:
    st.header("Left Column")
    st.write("Content for the left column.")

with col2:
    st.header("Right Column")
    st.write("Content for the right column.")

# Footer section
st.markdown("""
    ---
    <footer style='text-align: center; padding: 10px;'>
    <p>Created with Streamlit | My Website</p>
    </footer>
""", unsafe_allow_html=True)
