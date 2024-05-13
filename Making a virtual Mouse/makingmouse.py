
# import handtrackingmodule as htm
# import cv2
# import numpy as np
# import time
# import pyautogui

# pyautogui.FAILSAFE = False


# sensitivity = 4
# plocX,plocY = 0,0
# clocX,clocY = 0,0


# wCam = 640
# hCam = 488
# frameR = 100
# cap = cv2.VideoCapture(0)
# cap.set(3,wCam)
# cap.set(4,hCam)
# detector = htm.handDetector(maxHands=1)
# wScr,hScr = pyautogui.size()
# # print(wScr,hScr)
# while True:


#     #-->1 handLandmark
#     frame, img = cap.read()
#     img = detector.findhands(img=img)
#     lmlist,bbox = detector.findposition(img=img)
#     # print(lmlist)
#     #-->2 getting indexfinger and thumb index
#     # print(lmlist)
#     if(len(lmlist)!=0):
#         # print(lmlist)
#         x1 , y1 = lmlist[8][1:]
#         x2 , y2 = lmlist[12][1:]
#         # print(x1,y1,x2,y2)

#     #-->3 checking number of upped fingers
#     finger = detector.fingersUp()
#     # print(finger)
#     cv2.rectangle(img=img,pt1 = (frameR,frameR),pt2 = (wCam - frameR,hCam - frameR),color=(0,255,0),thickness=4,)
#     #-->4 only index finger:
#     if finger[1] == 1 and finger[2] == 0:

#         x3 = np.interp(x1,(frameR,wCam-frameR),(0,wScr))
#         y3 = np.interp(y1,(frameR,hCam-frameR),(0,hScr))
#         # x4 = np.interp(x2,(0,wCam),(0,wScr))
#         # y4 = np.interp(y2,(0,hCam),(0,hScr))
#         clocX = (plocX) + (x3 - plocX)/sensitivity
#         clocY = (plocY) + (y3 - plocY)/sensitivity
#         pyautogui.moveTo(plocX,plocY)
#         # cv2.circle(img,(x3,y3),5,(255,0,255),cv2.FILLED)
#         plocX,plocY = clocX,clocY        

#     #reducing the shaking


#     #-->clicking 
#     if finger[1] == 1 and finger[2] == 1:
#         distance,img,line_info = detector.finddistance(8,12,img)
#         print(distance)
#         if distance < 50:
#             cv2.circle(img,(line_info[4],line_info[5]),15,(255,192,203),cv2.FILLED)
#             pyautogui.click(x = plocX,y = plocY)


#     cv2.imshow("Image",img)
#     cv2.waitKey(1)



import cv2
import numpy as np
import handtrackingmodule as htm
import time
import pyautogui

######################
wCam, hCam = 640, 480
frameR = 100     #Frame Reduction
smoothening = 7  #random value
######################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = pyautogui.size()

# print(wScr, hScr)

while True:
    # Step1: Find the landmarks
    success, img = cap.read()
    img = detector.findhands(img)
    lmList, bbox = detector.findposition(img)

    # Step2: Get the tip of the index and middle finger
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # Step3: Check which fingers are up
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)

        # Step4: Only Index Finger: Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:

            # Step5: Convert the coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # Step6: Smooth Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Step7: Move Mouse
            pyautogui.moveTo(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # Step8: Both Index and middle are up: Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:

            # Step9: Find distance between fingers
            length, img, lineInfo = detector.finddistance(8, 12, img)

            # Step10: Click mouse if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.rightClick()

    # Step11: Frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (28, 58), cv2.FONT_HERSHEY_PLAIN, 3, (255, 8, 8), 3)

    # Step12: Display
    cv2.imshow("Image", img)