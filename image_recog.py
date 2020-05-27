import cv2
import numpy
import math
import sys


class Target:

    def __init__(self, _box, _frame):
        self.x = int(_box[0])
        self.y = int(_box[1])
        self.w = int(_box[2])
        self.h = int(_box[3])

        self.tracker = cv2.TrackerCSRT_create()
        self.tracker.init(_frame, (_box[0], _box[1], _box[2], _box[3]))
        self.items = []

    def update(self, frame):
        # getting the new coordinates from box and converting to int
        _, box = self.tracker.update(frame)
        self.x = int(box[0])
        self.y = int(box[1])
        self.w = int(box[2])
        self.h = int(box[3])

        # drawing the rectangle at new location
        cv2.rectangle(frame, (self.x, self.y),
                      (self.x + self.w, self.y + self.h), (200, 0, 200), 5, 1)

        # drawing the text next to the rectangle in a column
        y = 0
        for y, item in enumerate(self.items):
            cv2.putText(frame, item, (int(self.x) + int(self.w),
                                      int(self.y) + 25 * y), cv2.QT_FONT_BLACK, 1, (0, 0, 0), 1)

vidcap = cv2.VideoCapture("Souf.m4v")
success, frame = vidcap.read()
targets = [Target((353, 123, 51, 22), frame), Target((509, 108, 104, 73), frame)]


if len(sys.argv) > 1:
    print("HELLO")
    print(cv2.selectROI("_", frame));cv2.destroyWindow("_")
    quit(0)

while True:


    success, frame = vidcap.read()
    if cv2.waitKey(1) == ord('q') or not success:
        break

    for t in targets:
        t.update(frame)

    cv2.rectangle(frame, (114, 326), (130, 347), (200, 0, 0), 1, 0)
    cv2.imshow("cv2", frame)
