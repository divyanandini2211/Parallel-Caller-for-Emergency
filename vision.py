from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import sqlite3

# Function to generate response based on input and image
def get_gemini_response(input, image):
    # Define the GenerativeAI model
    model = genai.GenerativeModel("gemini-pro-vision")
    
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
              
    return response.text

# Function to save response to the database
def save_response_to_db(input_prompt, image, response, department):
    # Connect to the respective department's database
    conn = sqlite3.connect(f'{department}_complaints.db')
    c = conn.cursor()

    # Create complaints table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS complaints (
                    id INTEGER PRIMARY KEY,
                    input_prompt TEXT,
                    image BLOB,
                    response TEXT
                )''')

    # Convert PIL image to bytes
    if image:
        img_byte_arr = image.tobytes()
    else:
        img_byte_arr = None

    # Insert complaint details into the database
    c.execute("INSERT INTO complaints (input_prompt, image, response) VALUES (?, ?, ?)", 
              (input_prompt, img_byte_arr, response))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to extract department name from input prompt
def extract_department(input_prompt):
    # Extract department name from the input prompt
    # For simplicity, let's assume the department name is the first word of the input prompt
    words = input_prompt.split()
    if words:
        return words[0].lower()  # We'll convert to lowercase for consistency
    else:
        return "other"  # Default department if department name not found

# Define the main app function
def app():
    st.header("Complaints")
    input_prompt = st.text_input("Input prompt: ", key="input2")

    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    image = ""

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    submit = st.button("Tell me about the image") 

    if submit:
        response = get_gemini_response(input_prompt, image)
        st.subheader("The Response is")
        st.write(response)

        # Extract department name from the input prompt
        department = extract_department(input_prompt)

        # Save response to the department's database
        save_response_to_db(input_prompt, image, response, department)  

# Run the app








    








