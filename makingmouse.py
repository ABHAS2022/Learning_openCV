import handtrackingmodule as htm
import cv2
import numpy as np
import time
import pyautogui

pyautogui.FAILSAFE = False


sensitivity = 5
plocX,plocY = 0,0
clocX,clocY = 0,0


wCam = 640
hCam = 488
frameR = 100
cap = cv2.VideoCapture(1)
cap.set(3,wCam)
cap.set(4,hCam)
detector = htm.handDetector(maxHands=1)
wScr,hScr = pyautogui.size()
# print(wScr,hScr)
while True:


    #-->1 handLandmark
    frame, img = cap.read()
    img = detector.findhands(img=img)
    lmlist,bbox = detector.findposition(img=img)
    # print(lmlist)
    #-->2 getting indexfinger and thumb index
    # print(lmlist)
    if(len(lmlist)!=0):
        # print(lmlist)
        x1 , y1 = lmlist[8][1:]
        x2 , y2 = lmlist[12][1:]
        # print(x1,y1,x2,y2)

    #-->3 checking number of upped fingers
    finger = detector.fingersUp()
    # print(finger)
    cv2.rectangle(img=img,pt1 = (frameR,frameR),pt2 = (wCam - frameR,hCam - frameR),color=(0,255,0),thickness=4,)
    #-->4 only index finger:
    if finger[1] == 1 and finger[2] == 0:

        x3 = np.interp(x1,(frameR,wCam-frameR),(0,wScr))
        y3 = np.interp(y1,(frameR,hCam-frameR),(0,hScr))
        # x4 = np.interp(x2,(0,wCam),(0,wScr))
        # y4 = np.interp(y2,(0,hCam),(0,hScr))
        clocX = (plocX) + (x3 - plocX)/sensitivity
        clocY = (plocY) + (y3 - plocY)/sensitivity
        pyautogui.move(plocX,plocY)
        plocX,plocY = clocX,clocY        

    #reducing the shaking


    #-->clicking 
    if finger[1] == 1 and finger[2] == 1:
        distance,img,line_info = detector.finddistance(8,12,img)
        print(distance)
        if distance < 30:
            cv2.circle(img,(line_info[4],line_info[5]),15,(255,0,255),cv2.FILLED)
            pyautogui.click(x = line_info[4],y = line_info[5])


    cv2.imshow("Image",img)
    cv2.waitKey(1)