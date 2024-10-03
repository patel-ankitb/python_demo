import cv2
import dlib
from imutils import face_utils
from keras.models import load_model
import numpy as np

# Load pre-trained face detector from Dlib
detector = dlib.get_frontal_face_detector()

# Load pre-trained facial expression recognition model (you can replace this with your model)
model = load_model('path/to/your/model.h5')

# Define facial expression labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Function to detect and recognize facial expressions
def detect_and_recognize_expression(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    for face in faces:
        # Get facial landmarks
        shape = face_utils.shape_to_np(face)
        
        # Extract the region of interest (ROI) for facial expression recognition
        (x, y, w, h) = face_utils.rect_to_bb(face)
        roi = gray[y:y + h, x:x + w]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype('float') / 255.0
        roi = np.expand_dims(roi, axis=0)
        roi = np.reshape(roi, (1, 48, 48, 1))

        # Predict facial expression
        emotion_prediction = model.predict(roi)[0]
        emotion_label = emotion_labels[np.argmax(emotion_prediction)]

        # Draw the bounding box and emotion label on the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame

# Open the video capture
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Detect and recognize facial expressions
    frame = detect_and_recognize_expression(frame)

    # Display the frame
    cv2.imshow('Facial Expression Recognition', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
