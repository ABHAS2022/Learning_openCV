import handtrackingmodule as htm
import cv2
import numpy as np
import time
import pyautogui


cap = cv2.VideoCapture(1)
detector = htm.handDetector(maxHands=1)
while True:
    frame, img = cap.read()
    img = detector.findhands(img=img)
    lmlist = detector.findposition(img=img)
    if(lmlist!=0):
        x1,y1 = lmlist[]
    cv2.imshow("Image",img)
    cv2.waitKey(1)