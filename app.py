from flask import Flask, render_template, Response
import cv2
import base64
import requests

app = Flask(__name__)

# Gemini Pro Vision API endpoints
TEXT_DETECTION_URL = "https://api.geminiprovision.com/v1/ocr"
HANDWRITING_RECOGNITION_URL = "https://api.geminiprovision.com/v1/ocr/handwriting"

# Your Gemini Pro Vision API key
API_KEY = "YOUR_API_KEY"

def detect_text(frame):
    # Convert frame to base64 encoding
    _, buffer = cv2.imencode('.jpg', frame)
    image_base64 = base64.b64encode(buffer).decode('utf-8')

    # Make API call to Gemini Pro Vision for text detection
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "image": image_base64
    }
    try:
        response = requests.post(TEXT_DETECTION_URL, json=data, headers=headers)
        response.raise_for_status()  # Raise exception for 4XX and 5XX status codes
        result = response.json()

        # Process result and draw bounding boxes around detected text

    except requests.exceptions.RequestException as e:
        print("Error during text detection API call:", e)
        # Handle error appropriately, e.g., return original frame

    return frame

def recognize_handwriting(frame):
    # Convert frame to base64 encoding
    _, buffer = cv2.imencode('.jpg', frame)
    image_base64 = base64.b64encode(buffer).decode('utf-8')

    # Make API call to Gemini Pro Vision for handwriting recognition
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "image": image_base64
    }
    try:
        response = requests.post(HANDWRITING_RECOGNITION_URL, json=data, headers=headers)
        response.raise_for_status()  # Raise exception for 4XX and 5XX status codes
        result = response.json()

        # Process result and extract recognized handwriting

    except requests.exceptions.RequestException as e:
        print("Error during handwriting recognition API call:", e)
        # Handle error appropriately, e.g., return original frame

    return frame

def webcam_stream():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Detect and recognize text using Gemini Pro Vision
        frame = detect_text(frame)
        frame = recognize_handwriting(frame)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(webcam_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
