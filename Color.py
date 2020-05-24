import numpy as np
import cv2  

cap = cv2.VideoCapture('Vid.mp4')

while True:
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_white = np.array([0,255,0])
    upper_white = np.array([0,0,0])
    mask = cv2.inRange (hsv, lower_white, upper_white)
    bluecnts = cv2.findContours(mask.copy(),
                              cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(bluecnts)>0:
        blue_area = max(bluecnts, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(blue_area)
        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,255,255),2)

    cv2.imshow('frame',cv2.flip(frame, 0))
    cv2.imshow('mask',mask)

    k = cv2.waitKey(5) 
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()