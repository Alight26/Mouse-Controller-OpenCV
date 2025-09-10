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
            landmarks = hand_landmarks.landmark
            index_finger_tip = landmarks[8]

            x = int(index_finger_tip.x * w)
            y = int(index_finger_tip.y * h)

            screen_x = np.interp(x,[0,w],[0,screen_width])
            screen_y = np.interp(y,[0,h],[0,screen_height])

            pyautogui.moveTo(screen_x, screen_y)

            # Draws the hand landmarks
            mp_draw.draw_landmarks(img, hand_landmarks,mp_hands.HAND_CONNECTIONS)











    cv.imshow('img', img)
    k = cv.waitKey(1) & 0xff
    if k == ord('q'):
        break 


cap.release()
cv.destroyAllWindows()

