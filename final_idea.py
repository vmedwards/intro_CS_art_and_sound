from __future__ import annotations
import cv2
import turtle


# STEP 1: Import the necessary modules.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# Setup Turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)


cap = cv2.VideoCapture(0)

# STEP 2: Create an HandLandmarker object.
#base_options = python.BaseOptions(model_asset_path = 'hand_landmarker.task')
#options = vision.HandLandmarkerOptions(base_options = base_options, num_hands = 1)
#detector = vision.HandLandmarker.create_from_options(options)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue
    """
    
    # Flip the frame horizontally for natural movement
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # STEP 4: Detect hand landmarks from the input image.
    #results = detector.detect(rgb_frame)

    # STEP 5: Process the classification result. In this case, visualize it.
    #annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
    #cv2_imshow(cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract Index Finger Tip (Landmark 8)
            index_tip = hand_landmarks.landmark[8]
            
            # Convert normalized coordinates to screen coordinates
            x = int(index_tip.x * 640) - 320 # Adjust center
            y = -int(index_tip.y * 480) + 240 # Adjust center
            
            t.goto(x, y)
            # Add gesture logic (e.g., if index finger is up)
            # t.pendown() or t.penup()
    """
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

