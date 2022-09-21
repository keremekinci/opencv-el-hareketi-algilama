import time
import cv2
import mediapipe as mp

cap =cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands =mphands.Hands()
mpDraw= mp.solutions.drawing_utils
pTime=0
cTime=0
while 1:
    lmList = []
    succes, img =cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        handLms=results.multi_hand_landmarks[0]
        for id,lm in enumerate(handLms.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])
            cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)
            cv2.putText(img, str((id,cy)), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 
3)
        if len(lmList) != 0:
            baş_parmak_x = lmList[4][1]
            baş_parmak_y = lmList[4][2]
            orta_parmak_y=lmList[10][2]
            print(lmList[5][1], "-", baş_parmak_x)
            if lmList[5][1] < baş_parmak_x < lmList[9][1] and lmList[8][2]>baş_parmak_y:
                cv2.putText(img, str(("nah cekme")), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, 
(255, 0, 255), 3)
            elif lmList[15][2]>orta_parmak_y and lmList[7][2]>orta_parmak_y and 
lmList[20][2]>orta_parmak_y and lmList[10][2]-lmList[11][2]>80:
                cv2.putText(img, str(("orta parmak")), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, 
(255, 0, 255), 3)

        mpDraw.draw_landmarks(img,handLms,mphands.HAND_CONNECTIONS)

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(1000,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow("image",img)
    cv2.waitKey(1)
