from flask import Flask, send_from_directory, request, jsonify
from flask_sock import Sock
import os
import cv2
import mediapipe as mp
import base64
import numpy as np
from tensorflow.keras.models import load_model
import logging
import json

logging.basicConfig(level=logging.INFO)

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend')
sock = Sock(app)

# Load pre-trained model (update with actual model path)
try:
    model = load_model('models/gesture_model_2.keras')
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")

# Initialize MediaPipe
try:
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    logging.info("MediaPipe hands initialized successfully.")
except Exception as e:
    logging.error(f"Error initializing MediaPipe hands: {e}")

@app.route('/')
def index():
    return send_from_directory(app.template_folder, 'index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

@sock.route('/ws')
def websocket(ws):
    while True:
        data = ws.receive()
        if data is None:
            break
        try:
            data = json.loads(data)
            frame_data = data['frame']
            frame_data = frame_data.split(",")[1]  # Remove data:image/jpeg;base64,
            frame = base64.b64decode(frame_data)
            np_arr = np.frombuffer(frame, np.uint8)
            image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            # Process image and make prediction
            gesture = predict_gesture(image)
            ws.send(json.dumps({"gesture": gesture}))
        except Exception as e:
            logging.error(f"Error processing frame: {e}")
            ws.send(json.dumps({"gesture": "error"}))

def predict_gesture(image):
    # Convert image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process image with MediaPipe
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract landmarks for prediction
            landmarks = []
            for landmark in hand_landmarks.landmark:
                landmarks.append([landmark.x, landmark.y, landmark.z])

            logging.info(f"Extracted landmarks: {landmarks}")

            # Convert landmarks to numpy array for model input
            landmarks_np = np.array(landmarks).flatten().reshape(1, -1)

            # Normalize landmarks (assuming normalization was done during training)
            landmarks_np = landmarks_np / np.linalg.norm(landmarks_np)

            logging.info(f"Normalized landmarks: {landmarks_np}")

            # Make prediction with model
            prediction = model.predict(landmarks_np)
            gesture_index = np.argmax(prediction, axis=1)[0]

            logging.info(f"Predicted gesture index: {gesture_index}")

            # Map gesture index to gesture name
            gesture = gestures[gesture_index]
            logging.info(f"Predicted gesture: {gesture}")
            return gesture

    logging.info("No landmarks detected, returning unknown_gesture")
    return "unknown_gesture"

if __name__ == '__main__':
    logging.info("Starting Flask server...")
    app.run(debug=True)
