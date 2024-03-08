import cv2
import mediapipe as mp
import time
import ctypes
import pyautogui


lis = []
cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils


prevTime = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    user32 = ctypes.windll.user32
    screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    frame_height, frame_width, _ = img.shape

    scaleWidth = float(screen_width)/float(frame_width)
    scaleHeight = float(screen_height)/float(frame_height)

    if scaleHeight>scaleWidth:
            imgScale = scaleWidth

    else:
        imgScale = scaleHeight

    newX,newY = img.shape[1]*imgScale, img.shape[0]*imgScale
    img = cv2.resize(img,(int(newX),int(newY)))


    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if(results.multi_hand_landmarks):
        for handLMS in results.multi_hand_landmarks:
            for id, lms in enumerate(handLMS.landmark):
                # h,w,c = img.shape
                cx, cy = int(lms.x*newX) ,int(lms.y*newY)
                if id == 8:
                    print([id,cx,cy])
                    pyautogui.moveTo(cx,cy)
                    cv2.circle(img,(cx,cy),15,(235,92,39),cv2.FILLED)


            mpdraw.draw_landmarks(img,handLMS,mphands.HAND_CONNECTIONS)



    currTime = time.time()
    fps = 1/(currTime - prevTime)
    prevTime = currTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),1)
    cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    cv2.imshow("Video",img)
    cv2.waitKey(1)
