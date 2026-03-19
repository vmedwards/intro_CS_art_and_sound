from __future__ import annotations
import cv2
import mediapipe as mp
import turtle

# Setup Turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: continue

    # Flip the frame horizontally for natural movement
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

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

    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
