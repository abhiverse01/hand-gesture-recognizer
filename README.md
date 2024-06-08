<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hand Gesture Recognition Project</title>
</head>
<body>
    <h1>Hand Gesture Recognition</h1>

    <h2>Overview</h2>
    <p>
        A web application that recognizes and translates hand gestures into commands or text using a webcam. This project leverages computer vision and machine learning techniques to provide real-time hand gesture recognition capabilities.
    </p>

    <h2>Features</h2>
    <ul>
        <li>Recognizes predefined gestures.</li>
        <li>Displays corresponding action or text on the screen.</li>
    </ul>

    <h2>File Structure</h2>
    <pre>
    hand_gesture_recognition/
    ├── dataset/
    │   └── &lt;gesture_name&gt;/
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
    </pre>

    <h2>Setup</h2>
    <ol>
        <li>Create a virtual environment and activate it:
            <pre><code>python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`</code></pre>
        </li>
        <li>Install dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Run the Flask app:
            <pre><code>python src/backend/app.py</code></pre>
        </li>
    </ol>

    <h2>Development Phases</h2>
    <h3>Phase 1: Initial Setup and Data Collection</h3>
    <p>
        The initial phase involved setting up the project structure and collecting data for training the gesture recognition model. The dataset was organized into different folders, each representing a different gesture.
    </p>
    <h3>Phase 2: Model Training</h3>
    <p>
        During this phase, a convolutional neural network (CNN) was developed and trained using the collected gesture images. The model was fine-tuned for better accuracy and saved in the `models` directory.
    </p>
    <h3>Phase 3: Backend Development</h3>
    <p>
        A Flask-based backend was developed to handle the gesture recognition logic. The backend includes API endpoints for processing the images and returning the recognized gestures.
    </p>
    <h3>Phase 4: Frontend Development</h3>
    <p>
        The frontend was developed using HTML, CSS, and JavaScript. The web interface allows users to interact with the application and view the recognized gestures in real-time.
    </p>
    <h3>Phase 5: Integration and Testing</h3>
    <p>
        The final phase involved integrating the frontend and backend, followed by extensive testing to ensure the application works seamlessly. Bug fixes and performance improvements were made during this phase.
    </p>

    <h2>Current Updates</h2>
    <ul>
        <li>Improved model accuracy through additional training data and hyperparameter tuning.</li>
        <li>Enhanced frontend with better UI/UX for a smoother user experience.</li>
        <li>Added more predefined gestures and corresponding actions.</li>
        <li>Fixed bugs related to real-time gesture recognition and model loading.</li>
    </ul>

    <h2>How to Contribute</h2>
    <p>
        Contributions are welcome! Please follow the steps below to contribute to this project:
    </p>
    <ol>
        <li>Fork the repository on GitHub.</li>
        <li>Create a new branch for your feature or bugfix.</li>
        <li>Make your changes and commit them with descriptive messages.</li>
        <li>Push your changes to your forked repository.</li>
        <li>Submit a pull request to the main repository.</li>
    </ol>

    <h2>License</h2>
    <p>
        This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.
    </p>

    <h2>Contact</h2>
    <p>
        For any questions or inquiries, please contact me at <a href="mailto:your_email@example.com">www.abhishekshah007@example.com</a>.
    </p>
</body>
</html>
