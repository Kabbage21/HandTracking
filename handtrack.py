# import necessary packages for hand gesture recognition project using Python OpenCV
import cv2
import mediapipe as mp

#Initializing hand
mpHand = mp.solutions.hands
Hands = mpHand.Hands()
#To be able to track
mpDraw = mp.solutions.drawing_utils

webcam = cv2.VideoCapture(0)

while True:
    success,img = webcam.read()
    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = Hands.process(converted_image)

    if result.multi_hand_landmarks:
        for hand_frame in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,hand_frame,mpHand.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracking",img)
    key = cv2.waitKey(1)
    if key == 113 or key == 81:
        break