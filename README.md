# Hand Gesture Recognition

## Overview

A web application that recognizes and translates hand gestures into commands or text using a webcam. This project leverages computer vision and machine learning techniques to provide real-time hand gesture recognition capabilities.

## Features

- Recognizes predefined gestures.
- Displays corresponding action or text on the screen.

## File Structure

```plaintext
hand_gesture_recognition/
├── dataset/
│   └── <gesture_name>/
│       └── *.png
├── src/
│   ├── frontend/
│   │   ├── index.html
│   │   └── static/
│   │       ├── css/
│   │       │   └── styles.css
│   │       └── js/
│   │           └── script.js
│   ├── backend/
│   │   ├── app.py
│   │   ├── api/
│   │   │   └── endpoints.py
│   │   └── models/
│   │       └── gesture_model.h5
│   └── scripts/
│       └── add_gestures.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup
1. Create a virtual environment and activate it:
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

2. Install dependencies:
    pip install -r requirements.txt

3. Run the Flask app:
    python src/backend/app.py

## Development Phases
1. Phase 1: Initial Setup and Data Collection
    The initial phase involved setting up the project structure and collecting data for training the gesture recognition model. The dataset was organized into different folders, each representing a different gesture.

2. Phase 2: Model Training
    During this phase, a convolutional neural network (CNN) was developed and trained using the collected gesture images. The model was fine-tuned for better accuracy and saved in the models directory.

3. Phase 3: Backend Development
    A Flask-based backend was developed to handle the gesture recognition logic. The backend includes API endpoints for processing the images and returning the recognized gestures.

4. Phase 4: Frontend Development
    The frontend was developed using HTML, CSS, and JavaScript. The web interface allows users to interact with the application and view the recognized gestures in real-time.

5. Phase 5: Integration and Testing
    The final phase involved integrating the frontend and backend, followed by extensive testing to ensure the application works seamlessly. Bug fixes and performance improvements were made during this phase.

## Current Updates
1. Improved model accuracy through additional training data and hyperparameter tuning.
2. Enhanced frontend with better UI/UX for a smoother user experience.
3. Added more predefined gestures and corresponding actions.
4. Fixed bugs related to real-time gesture recognition and model loading.

## How to Contribute
Contributions are welcome! Please follow the steps below to contribute to this project:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any questions or inquiries, please contact me at www.abhishekshah007@example.com.











