import cv2
import os
import sys

if len(sys.argv) != 3:
    print("Usage: python add_gestures.py <gesture_name> <num_of_images>")
    sys.exit()

gesture_name = sys.argv[1]
num_images = int(sys.argv[2])

# Create directory for the gesture if it doesn't exist
gesture_dir = f'../../gestures/{gesture_name}'
os.makedirs(gesture_dir, exist_ok=True)

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    sys.exit()

print(f"Collecting {num_images} images for gesture '{gesture_name}'. Press 'A' to start.")

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('frame', frame)

    # Start capturing images when 'A' is pressed
    if cv2.waitKey(1) & 0xFF == ord('a'):
        for i in range(num_images):
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            img_name = os.path.join(gesture_dir, f'{gesture_name}_{count}.png')
            cv2.imwrite(img_name, frame)
            count += 1
            print(f'Image {count} saved: {img_name}')

            # Display the captured image
            cv2.imshow('frame', frame)
            cv2.waitKey(100)  # Delay to simulate capturing frames over time

        break

cap.release()
cv2.destroyAllWindows()
