import cv2
import numpy as np
import time

fc = cv2.CascadeClassifier('ff.xml')

fc2 = cv2.CascadeClassifier('cc.xml')

cap = cv2.VideoCapture('yasin.mp4')

while True:

    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = fc2.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:

        text = "Y"

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, text, (x - 20, y + 40), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)

        r_gray = gray[y:y+h, x:x+w]

        r_color = img[y:y+h, x:x+w]

        face2 = fc.detectMultiScale(gray, 1.1, 4)

        for (x2, y2, w2, h2) in face2:

            text = "X"

            cv2.rectangle(r_color, (y2,y2), (x2+w2, y2+h2), (0, 255, 0), 4)
            cv2.putText(img, text, (x - 20, y + 40), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
        
    #cv2.resize(img, cv2.WINDOW_NORMAL)

    img2 = cv2.resize(img,None,fx=0.4,fy=0.4)

    j = dst=cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow("img", j)

    k = cv2.waitKey(30) & 0xff
    
    if k==27:

        break

cap.release()
cv2.destroyAllWindows()