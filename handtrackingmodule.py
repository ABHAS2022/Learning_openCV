import cv2
import mediapipe as mp
import time
# import pyautogui
import math
# 



# prevTime = 0

# while True:
#     success, img = cap.read()


#     currTime = time.time()
#     fps = 1/(currTime - prevTime)
#     prevTime = currTime
#     cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),1)



    # cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
    # cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, 0)
    # cv2.imshow("Video",img)
    # cv2.waitKey(1)




class handDetector():
    def __init__(self,mode = False,maxHands = 2, detectionconf = 0.5,trackconf = 0.5,modelComplexity = 1):
        self.mode = mode
        self.modelComplexity = modelComplexity
        self.maxHands = maxHands
        self.detectionconf = detectionconf
        self.trackconf = trackconf

        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode,self.maxHands,self.modelComplexity,self.detectionconf,self.trackconf)
        self.mpdraw = mp.solutions.drawing_utils


    def findhands(self,img,draw = True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        if(results.multi_hand_landmarks):
            for handLMS in results.multi_hand_landmarks:
                if (draw):
                    self.mpdraw.draw_landmarks(img,handLMS,self.mphands.HAND_CONNECTIONS)
        return img
                        # for id, lms in enumerate(handLMS.landmark):
                        # # print(id,lms)
                        # h,w,c = img.shape
                        # cx, cy = int(lms.x*w) ,int(lms.y*h)
                        # print(id,cx,cy)
                        # if id == 8:
                        #     cv2.circle(img,(cx,cy),15,(235,92,39),cv2.FILLED)

    def findposition(self,img,handnumber = 0,draw = True):
        lmslist = []
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        if(results.multi_hand_landmarks):
                myHand = results.multi_hand_landmarks[handnumber]
            # for handLMS in results.multi_hand_landmarks:
                for id, lms in enumerate(myHand.landmark):
                    # print(id,lms)
                    h,w,c = img.shape
                    cx, cy = int(lms.x*w) ,int(lms.y*h)
                    # print(id,cx,cy)
                    lmslist.append([id,cx,cy])
                    # if id == 8:
                    if draw:
                        cv2.circle(img,(cx,cy),7,(235,92,39),cv2.FILLED)        
        return lmslist
    def finddistance(self,p1,p2,img,draw=True,r = 15,t = 3):
        x1,y1 = self.lmlist[p1][1:]           
        x2,y2 = self.lmlist[p2][1:]
        cx,cy = (x1+x2)//2, (y1+y2)//2

        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,0,255),t)
            cv2.circle(img,(x1,x2),r,(255,0,255),cv2.FILLED)
            cv2.circle(img,(cx,cy),r,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),r,(0,0,255),cv2.FILLED)
        length = math.hypot(x2-x1,y2-y1)


        return length,img,[x1,y1,x2,y2,cx,cy]


def main():

    cap = cv2.VideoCapture(1)
    currTime = 0
    prevTime = 0
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findhands(img)
        lmlist = detector.findposition(img,0)
        if len(lmlist)!=0:
            print(lmlist[4])
        currTime = time.time()
        fps = 1/(currTime - prevTime)
        prevTime = currTime
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),1)
        cv2.imshow("Video",img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()