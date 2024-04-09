from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import cv2
from PIL import Image
import numpy as np
import sqlite3

# Load the GenerativeAI model
model = genai.GenerativeModel("gemini-pro-vision")

# Function to process webcam frames and generate response
def get_gemini_response(frame):
    # Convert frame to PIL Image
    pil_image = Image.fromarray(frame)

    # Generate response using the model
    response = model.generate_content(pil_image)

    return response.text

# Function to create table if not exists
def create_table_if_not_exists():
    conn = sqlite3.connect('emergency.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS emergency_responses
                 (frame_image BLOB, response TEXT)''')
    conn.commit()
    conn.close()

# Function to save response to the database
def save_response_to_db(frame_image, response):
    # Connect to the database
    conn = sqlite3.connect('emergency.db')
    c = conn.cursor()

    # Insert response into the database
    c.execute("INSERT INTO emergency_responses (frame_image, response) VALUES (?, ?)", 
              (frame_image, response))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Function to capture video frames from webcam
def capture_frames():
    # Open webcam
    cap = cv2.VideoCapture(0)

    # Continuously capture frames from webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Display frame
        st.image(frame, caption='Live Webcam Feed', use_column_width="50")

        # Generate response
        response = get_gemini_response(frame)

        # Display response
        st.subheader("The Response is")
        st.write(response)

        # Save response to the database
        save_response_to_db(frame.tobytes(), response)

        # Check for user input to stop capturing frames
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()

# Define the main app function
def app():
    # Streamlit configuration
    st.header("EMERGENCY CALL")

    # Create table if it doesn't exist
    create_table_if_not_exists()

    # Button to start capturing webcam frames
    start_button = st.button("Start Live Webcam Feed",key="start_button")

    # When the start button is clicked, start capturing webcam frames
    if start_button:
        capture_frames()

# Call the app function to run the Streamlit app




