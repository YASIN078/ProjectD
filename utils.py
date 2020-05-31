import cv2
import numpy as np
import math
import sys

def DrawRect(frame, x, y, w, h, color = (200, 0, 0)):
    """Draws a rectangle in the given frame with the coordinates given"""
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 1, 0)


def CompareColors(c1, c2):
    """Returns a value between 0 and 442 compared to two colors"""
    return math.sqrt(
        (c1[0] - c2[0])**2 +
        (c1[1] - c2[1])**2 +
        (c1[2] - c2[2])**2
    )

def dist(p1, p2):
    """Returns the distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)




def GetClosestColor(frame, box, targetColor):
    """Returns the closest color's score compared to the target color"""
    # getting coordinates
    min_x = box[0]
    max_x = min_x + box[1]
    min_y = box[2]
    max_y = min_y + box[3]
    BEST_SCORE = 250
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            score = CompareColors(frame[y, x], targetColor)
            if score < BEST_SCORE:
                BEST_SCORE = score
    return BEST_SCORE

def CheckObject(frame, box, color):
    DrawRect(frame, box[0], box[1], box[2], box[3])
    return GetClosestColor(frame, box, color)


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
    def GetMiddle(self):
        return [self.x + self.w / 2, self.y + self.h / 2]



class Phone:
    def __init__(self, _name, _low_color, _high_color, _box):
        self.name = _name
        self.low_color = np.array(_low_color)
        self.high_color = np.array(_high_color)
        self.box = _box
        self.taken = False

    def Check(self, frame):
        """Check if phone is still there (return true if found inside frame)"""
        DrawRect(frame, self.box[0], self.box[1], self.box[2], self.box[3], (0, 0, 0))
        img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(img_hsv, self.low_color, self.high_color)
        img_result = cv2.bitwise_and(frame, frame, mask=mask)

        i = 0
        # for every pixel inside boundaries of phone
        for x in range(self.box[0], self.box[0] + self.box[2]):
            for y in range(self.box[1], self.box[1] + self.box[3]):
                p = img_result[y, x]
                if any(p) > 0:
                    return True
        return False

    def GetMiddle(self):
        return [
            self.box[0] + self.box[2] / 2,
            self.box[1] + self.box[3] / 2,
        ]
