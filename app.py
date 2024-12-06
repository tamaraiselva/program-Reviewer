import streamlit as st
import google.generativeai as genai

# Configure the Google Generative AI API
genai.configure(api_key="AIzaSyBIbJpxb6UDglfPtLeaG_TBGyxbtvFv0Tg")  # Replace with your actual API key

# Set up the app layout
st.title("Code Reviewer")
st.write("Enter your code below for review:")

# Text area for code input
user_code = st.text_area("Enter your code here...", height=200)

# Button to trigger code review
if st.button("Generate"):
    if user_code:
        # Initialize the generative model
        llm = genai.GenerativeModel("models/gemini-1.5-flash")
        
        # Send the user code for review
        chatbot = llm.start_chat(history=[])
        response = chatbot.send_message(f"Review the following Python code and identify any bugs:\n{user_code}")
        
        # Display the AI-generated response
        st.subheader("Code Review")
        st.write("Bug Report:")
        st.write(response.text)  # Display AI response