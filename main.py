import cv2 as cv 
import mediapipe as mp 


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence= 0.5,
                    min_tracking_confidence = 0.5)


cap = cv.VideoCapture(1)

while True:
    ret, img = cap.read()
    img = cv.flip(img, 1)

    if ret is False:
        break

    RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)







    cv.imshow('img', img)
    k = cv.waitKey(30) & 0xff
    if k == ord('q'):
        break 


cap.release()
cv.destroyAllWindows()

