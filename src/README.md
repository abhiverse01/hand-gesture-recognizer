# Hand Gesture Recognition

## Overview

A web application that recognizes and translates hand gestures into commands or text using a webcam.

## Features

- Recognizes predefined gestures.
- Displays corresponding action or text on the screen.

## File Structure

hand_gesture_recognition/
├── dataset/
│ └── <gesture_name>/
│ └── *.png
├── src/
│ ├── frontend/
│ │ ├── index.html
│ │ └── static/
│ │ ├── css/
│ │ │ └── styles.css
│ │ └── js/
│ │ └── script.js
│ ├── backend/
│ │ ├── app.py
│ │ ├── api/
│ │ │ └── endpoints.py
│ │ └── models/
│ │ └── gesture_model.h5
│ └── scripts/
│ └── add_gestures.py
├── requirements.txt
├── README.md
└── .gitignore

## Setup

1. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the Flask app:
    ```bash
    python src/backend/app.py

