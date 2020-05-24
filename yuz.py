import cv2
import numpy as np

fc = cv2.CascadeClassifier('cascade.xml')
#fc2 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('Vid.mp4')

while True:

    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = fc.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        '''face2 = fc.detectMultiScale(gray, 1.1, 4)
        for (x2, y2, w2, h2) in face2:
            cv2.rectangle(roi_color, (y2,y2), (x2+w2, y2+h2), (0, 255, 0), 4)'''

    cv2.imshow('img', cv2.flip(img, 0))

    k = cv2.waitKey(30) & 0xff
    
    if k==27:
        break

cap.release()