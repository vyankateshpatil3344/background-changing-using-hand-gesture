import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8)
segmentor =SelfiSegmentation()
listImg =os.listdir("BackgroundImages")
print(listImg)
imgList=[]
for imgPath in listImg:
    img=cv2.imread(f'BackgroundImages/{imgPath}')
    img=cv2.resize(img,(1280,720))
    imgList.append(img)
print(len(imgList))

indexImg=0

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("image", cv2.WND_PROP_AUTOSIZE, cv2.WINDOW_NORMAL)

while True:
    success,img=cap.read()
    imgOut=segmentor.removeBG(img,imgList[indexImg])
    hands, img = detector.findHands(img)

    print(indexImg)
    cv2.imshow("image",imgOut)
    key=cv2.waitKey(1)


    if(len(hands)==1):
        if detector.fingersUp(hands[0])==[0,1,0,0,0]:
                indexImg=0
        elif detector.fingersUp(hands[0])==[0,1,1,0,0]:
                indexImg=1
        elif detector.fingersUp(hands[0])==[0,1,1,1,0]:
                indexImg=2
        elif detector.fingersUp(hands[0])==[0,1,1,1,1]:
                indexImg=3
        elif detector.fingersUp(hands[0])==[1,0,0,0,0]:
            break