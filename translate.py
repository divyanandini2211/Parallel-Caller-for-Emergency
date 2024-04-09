from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from googletrans import Translator
import sqlite3

# Load the GenerativeAI model
model = genai.GenerativeModel("gemini-pro-vision")
translator = Translator()

# Function to process input prompt and image and generate response
def get_gemini_response(input, image):
    if input != "":
         response = model.generate_content([input, image])
    else:
          response = model.generate_content(image)
              
    # Translate the response to English
    translated_response = translator.translate(response.text, dest='en').text
    return translated_response

# Function to create table if it doesn't exist
def create_table_if_not_exists():
    conn = sqlite3.connect('complaints_responses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS complaints_responses
                 (input_prompt TEXT, image BLOB, response TEXT)''')
    conn.commit()
    conn.close()

# Function to save response to the database
def save_response_to_db(input_prompt, image, response):
    # Connect to the database
    conn = sqlite3.connect('complaints_responses.db')
    c = conn.cursor()

    # Convert PIL image to bytes
    if image:
        img_byte_arr = image.tobytes()
    else:
        img_byte_arr = None

    # Insert response into the database
    c.execute("INSERT INTO complaints_responses (input_prompt, image, response) VALUES (?, ?, ?)", 
              (input_prompt, img_byte_arr, response))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Define the main app function
def app():
    # Streamlit configuration
    st.header("Text Complaints")
    input_prompt = st.text_input("Input prompt: ", key="input3")

    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    image = ""

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    submit = st.button("Tell me about the image") 

    if submit:
        response = get_gemini_response(input_prompt, image)
        st.subheader("The Translated Response is")
        st.write(response)  

        # Save response to the database
        save_response_to_db(input_prompt, image, response)

# Create table if it doesn't exist
create_table_if_not_exists()

# Call the app function to run the Streamlit app




