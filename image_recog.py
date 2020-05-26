import cv2
import numpy as np
import math

vidcap = cv2.VideoCapture('Souf.m4v')
success, frame = vidcap.read()

# customer box tuple
# box = (18, 333, 113, 199) # PROCESSING ANIMATION
box = (505, 106, 112, 118)

# print(frame[313, 236])

tracker = cv2.TrackerCSRT_create()
tracker.init(frame, box)

# aquired = False

# selection box
# print(cv2.selectROI("_", frame));cv2.destroyWindow("_")

frameCount = 0

while success:
    # imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # _, imgray = cv2.threshold(imgray, 127, 100, cv2.THRESH_BINARY)

    # reading new frame and updating boxes
    success, frame = vidcap.read()
    _, box = tracker.update(frame)
    frameCount+=1

    p1 = (int(box[0]), int(box[1]))
    p2 = (int(box[0] + box[2]), int(box[1] + box[3]))

    cv2.rectangle(frame, p1, p2, (200, 0, 200), 5, 1)
    cv2.imshow("cv2", frame)

    if cv2.waitKey(1) == ord('q'):
        break


class Target:

    def __init__(self, _box, _frame):
        self.box = _box
        self.tracker = cv2.TrackerCSRT_create()
        self.tracker.init(frame, (box[0], box[1], box[2], box[3]))
        self.items = []

    def update(self, frame):
        _, self.box = tracker.update(frame)
        cv2.rectangle(frame, p1, p2, (200, 0, 200), 5, 1)










