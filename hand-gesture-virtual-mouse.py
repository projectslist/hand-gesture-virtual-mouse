import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import pyautogui



cam = cv2.VideoCapture(0)
pyautogui.FAILSAFE = False
detector = HandDetector(detectionCon=0.8, maxHands=2)

screen_w, screen_h = pyautogui.size()

while True:
    success,img = cam.read()

    # For left to left and right to right
    img = cv2.flip(img, 1)

    lmList, bboxInfo = detector.findHands(img)


    if lmList:
        l , _, _ = detector.findDistance(lmList[0]['lmList'][8][:2], lmList[0]['lmList'][12][:2], img)

        pyautogui.moveTo(lmList[0]['lmList'][8][:2])
        if l < 100:
            pyautogui.click()
            print('click')
            sleep(0.2)
    cv2.imshow('Virtual Mouse', img)
    cv2.waitKey(1)