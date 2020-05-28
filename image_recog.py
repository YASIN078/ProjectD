import cv2
import numpy
import math
import sys
from utils import *

vidcap = cv2.VideoCapture("Souf.m4v")
success, frame = vidcap.read()
targets = [Target((353, 123, 51, 22), frame), Target((509, 108, 104, 73), frame)]


# print(CompareColors([0, 0, 0], [255, 255, 255]))

if len(sys.argv) > 1:
    print("HELLO")
    print(cv2.selectROI("_", frame));cv2.destroyWindow("_")
    quit(0)

frameCount = 0
while True:
    if cv2.waitKey(1) == ord('q') or not success:
        break
    for t in targets:
        t.update(frame)

    # Red joycon [ 58  65 211] <= joycon color

    if CheckObject(frame, [79, 280, 66, 80], [58, 65, 200]) > 70:
        print("ROOD IS OPGEPAKT", frameCount)

    # Blue joycon
    if CheckObject(frame, [203, 225, 59, 90], [162, 147, 34]) > 80:
        print("BLAUW IS OPGEPAKT", frameCount)



    cv2.imshow("cv2", frame)

    success, frame = vidcap.read()
    success, frame = vidcap.read()
    success, frame = vidcap.read()
    success, frame = vidcap.read()
    success, frame = vidcap.read()
    success, frame = vidcap.read()

    frameCount+=1
