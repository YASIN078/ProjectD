import cv2
import numpy as np
import math
import sys

class Target:

    def __init__(self, _box, _frame):
        self.box = _box
        self.tracker = cv2.TrackerCSRT_create()
        self.tracker.init(frame, (_box[0], _box[1], _box[2], _box[3]))
        self.items = []

    def update(self, frame):
        _, self.box = self.tracker.update(frame)
        cv2.rectangle(frame,
        (
            int(self.box[0]), int(self.box[1])
        ),

          (
              int(self.box[0] + self.box[2]),
              int(self.box[1] + self.box[3]) )
                      , (200, 0, 200), 5, 1)




vidcap = cv2.VideoCapture('Souf.m4v')
success, frame = vidcap.read()

# if len(sys.argv) > 0:
#     # selection box
#     print(cv2.selectROI("_", frame));cv2.destroyWindow("_")
#     quit(0)

# customer box tuple
# box = (18, 333, 113, 199) # PROCESSING ANIMATION
# box = (505, 106, 112, 118)
targets = [Target((468, 98, 169, 194), frame), Target((350, 123, 78, 102), frame)]

# print(frame[313, 236])

# tracker = cv2.TrackerCSRT_create()
# tracker.init(frame, box)

# aquired = False




frameCount = 0

while success:
    # imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # _, imgray = cv2.threshold(imgray, 127, 100, cv2.THRESH_BINARY)
    # reading new frame and updating boxes
    success, frame = vidcap.read()
    for t in targets:
        t.update(frame)
    frameCount+=1

    # p1 = (int(box[0]), int(box[1]))
    # p2 = (int(box[0] + box[2]), int(box[1] + box[3]))

    # cv2.rectangle(frame, p1, p2, (200, 0, 200), 5, 1)
    cv2.imshow("cv2", frame)

    if cv2.waitKey(1) == ord('q'):
        break










