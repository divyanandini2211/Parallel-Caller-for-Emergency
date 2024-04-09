from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Configure GenerativeAI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Function to generate response to a question
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Define the main app function
def app():
    st.header("Chat")
    input_question = st.text_input("Input: ", key="input4")
    submit_button = st.button("Ask the question")

    if submit_button:
         response = get_gemini_response(input_question)
         st.subheader("The response is")
         st.write(response)

# Call the app function to run the Streamlit app




