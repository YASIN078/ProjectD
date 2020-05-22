import cv2
import numpy as np
import win32api
import funcs

cap = cv2.VideoCapture('Vid.mp4')
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))

ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
while cap.isOpened():
    try:
        diff = cv2.absdiff(frame1, frame2)
        #gray scale
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        rectangles = []
        for contour in contours:
            rectangles.append(cv2.boundingRect(contour))
        
        rectangles = funcs.reduceContours(rectangles)
        
        for rect in rectangles:
            (x, y, w, h) = rect
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 3)
            

        image = cv2.resize(frame1, (1280,720))
        out.write(image)
        cv2.imshow("feed", frame1)
        frame1 = frame2
        ret, frame2 = cap.read()

        if cv2.waitKey(40) == 27:
            break
    except:
        cv2.destroyAllWindows()
        cap.release()
        out.release()
        win32api.MessageBox(0,'Video Finished','Done!')

cv2.destroyAllWindows()
cap.release()
out.release()