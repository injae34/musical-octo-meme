# fire detection (finding number of red pixels)
from picamera import PiCamera
from time import sleep
import cv2 as cv
import numpy as np

camera = PiCamera()
sleep(0.1)

def system():
    camera.capture('picture.png')
    print("capture picture")

    fire = cv.imread('picture.png', 1)
    fire = cv.resize(fire, (960, 540))
    blur = cv.GaussianBlur(fire, (21, 21), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
    lower = np.array([-10, 50, 50])
    upper = np.array([10, 255, 255])
    mask = cv.inRange(hsv, lower, upper)

    output = cv.bitwise_and(fire, hsv, mask = mask)
    no_red = cv.countNonZero(mask)
    print("fire detect finish")
    cv.imwrite("output.png", output)
    #print(no_red)
    if int(no_red) > 10000:
        print("Fire Detected")
        result = 1
    else:
        result = 0
    return result

"""
while True:
    sleep(2)
    fire = system()
    sleep(5)
    if fire == 1:
        break
"""

