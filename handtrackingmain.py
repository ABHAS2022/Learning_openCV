import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils


prevTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if(results.multi_hand_landmarks):
        for handLMS in results.multi_hand_landmarks:
            for id, lms in enumerate(handLMS.landmark):
                # print(id,lms)
                h,w,c = img.shape
                cx, cy = int(lms.x*w) ,int(lms.y*h)
                print(id,cx,cy)
                if id == 8:
                    cv2.circle(img,(cx,cy),15,(235,92,39),cv2.FILLED)


            mpdraw.draw_landmarks(img,handLMS,mphands.HAND_CONNECTIONS)



    currTime = time.time()
    fps = 1/(currTime - prevTime)
    prevTime = currTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),1)



    # cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, 0)
    cv2.imshow("Video",img)
    cv2.waitKey(1)