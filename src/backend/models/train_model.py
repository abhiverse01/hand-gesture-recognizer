import os
import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dense, Flatten, Dropout, BatchNormalization
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO)

# Define gestures globally
gestures = ["boom", "thumbs_up", "victory", "yoyo"]

def load_data():
    data = []
    labels = []

    # Adjust the path to reach the gestures directory from the current script's location
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../gestures'))

    for label, gesture in enumerate(gestures):
        gesture_dir = os.path.join(base_dir, gesture)
        for img_name in os.listdir(gesture_dir):
            img_path = os.path.join(gesture_dir, img_name)
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (128, 128))
            data.append(img)
            labels.append(label)

            # Log a few examples
            if len(data) <= 5:  # Log only the first 5 examples
                logging.info(f"Training image shape: {img.shape}")
                logging.info(f"Training label: {label}")

    data = np.array(data)
    labels = np.array(labels)
    labels = to_categorical(labels)

    return data, labels

def create_model():
    model = Sequential([
        Input(shape=(128, 128, 3)),

        # First Convolutional Block
        Conv2D(32, kernel_size=(3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2)),

        # Second Convolutional Block
        Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2)),

        # Third Convolutional Block
        Conv2D(128, kernel_size=(3, 3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2, 2)),

        # Fully Connected Layers
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(128, activation='relu'),
        Dropout(0.5),

        # Output Layer
        Dense(len(gestures), activation='softmax')
    ])

    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

    return model

def plot_training_history(history):
    plt.figure(figsize=(12, 4))

    # Plot training & validation accuracy values
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')

    # Plot training & validation loss values
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')

    plt.show()

def main():
    data, labels = load_data()
    
    # Split data into training and validation sets
    x_train, x_val, y_train, y_val = train_test_split(data, labels, test_size=0.3, random_state=42)
    
    # Data Augmentation
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    # Callbacks
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.0001)

    model = create_model()
    
    history = model.fit(datagen.flow(x_train, y_train, batch_size=32),
                        epochs=35,
                        validation_data=(x_val, y_val),
                        callbacks=[early_stopping, reduce_lr],
                        verbose=1)
    
    model.save('models/gesture_model_2.keras')  # Save model in Keras format
    plot_training_history(history)

if __name__ == "__main__":
    main()
