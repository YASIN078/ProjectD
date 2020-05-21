import cv2
import numpy as np


class Motion:

    def __init__(self, video):
        self.video = video
    

    def capture_video(self):
        cap = cv2.VideoCapture(self.video)

        ret, frame1 = cap.read()
        ret, frame2 = cap.read()
        while cap.isOpened():
            try:
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (5,5), 0)
                _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=2)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                
                for contour in contours:
                    (x, y, w, h) = cv2.boundingRect(contour)
                    if cv2.contourArea(contour) < 900:
                        continue
                    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 3)
                    cv2.putText(frame1, "".format(), (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
                    cv2.putText(frame1, "".format(), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 3)
                cv2.imshow("feed", frame1)
                frame1 = frame2
                ret, frame2 = cap.read()

                if cv2.waitKey(40) == 27:
                    break
            except:
                cv2.destroyAllWindows()
                cap.release()

        cv2.destroyAllWindows()
        cap.release()


if __name__ == "__main__":
    m = Motion('Vid.mp4')
    m.capture_video()
    