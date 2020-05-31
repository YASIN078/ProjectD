import cv2
import numpy as np
import math
import sys
from utils import *

vidcap = cv2.VideoCapture("Souf.m4v")
success, frame = vidcap.read()


targets = [
    Target((353, 123, 51, 22), frame),
    Target((509, 108, 104, 73), frame)
]

phones = [
    Phone("Red joycon", [161, 155, 84], [179, 255, 255], [79, 280, 66, 70]),
    Phone("Blue joycon", [94, 80, 2], [126, 255, 255], [203, 225, 59, 90])
]

if len(sys.argv) > 1:
    print(cv2.selectROI("_", frame));cv2.destroyWindow("_")
    quit(0)

frameCount = 0
while True:
    if cv2.waitKey(1) == ord('q') or not success:
        break
    for t in targets:
        t.update(frame)


    # Only check for joycons N many frames
    if frameCount % 30 == 0:
        DrawRect(frame, 0, 0, 10, 10, (0, 0, 200))


        for p in phones:
            if p.Check(frame):
                pass
                # if the Phone was taken before and is now back in frame
                if p.taken:
                    for t in targets:
                        if p.name in t.items:
                            t.items.remove(p.name)
                    p.taken = False
            else:
                if p.taken:
                    continue
                bestD = 999999
                bestT = None
                for t in targets:
                    d = dist(t.GetMiddle(), p.GetMiddle())
                    if d < bestD:
                        bestD = d
                        bestT = t
                p.taken = True
                bestT.items.append(p.name)

    cv2.imshow("cv2", frame)
    success, frame = vidcap.read()

    frameCount+=1
