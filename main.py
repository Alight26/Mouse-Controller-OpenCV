import cv2 as cv 
import mediapipe as mp 
import pyautogui 
import numpy as np


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence= 0.7,
                    min_tracking_confidence = 0.7)


cap = cv.VideoCapture(1)

screen_width, screen_height = pyautogui.size()


while True:
    ret, img = cap.read()
    img = cv.flip(img, 1)

    if ret is False:
        break

    h, w, c = img.shape

    RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(RGB_img)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Draws the hand landmarks
            mp_draw.draw_landmarks(img, hand_landmarks,mp_hands.HAND_CONNECTIONS)











    cv.imshow('img', img)
    k = cv.waitKey(30) & 0xff
    if k == ord('q'):
        break 


cap.release()
cv.destroyAllWindows()

