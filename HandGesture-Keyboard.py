import cv2
import os
import mediapipe
import pyautogui
from cvzone.HandTrackingModule import HandDetector

# Cam setup
width, height = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, flipType=True)


    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print(fingers)


        if hand["lmList"][4][0] < hand["lmList"][17][0]:  # Check hand position for left/right determination
           # for left hand
            if fingers == [0, 1, 1, 0, 0]:
                pyautogui.press("left")
                pyautogui.sleep(1)
                print("Left")
            if fingers == [1, 0, 0, 0, 0]:
                pyautogui.press("space")
                pyautogui.sleep(1)
                print("space")
            if fingers == [0, 1, 0, 0, 0]:
                pyautogui.hotkey('alt', 'tab')
                pyautogui.sleep(1)
                print("alt+ tab")

        else: #for right hand
            if fingers == [0, 1, 1, 0, 0]:
                pyautogui.press("right")
                pyautogui.sleep(1)
                print("Right")
            if fingers == [1, 0, 0, 0, 0]:
                pyautogui.press("Esc")
                pyautogui.sleep(2)
                print("Esc")
            if fingers == [0, 1, 0, 0, 0]:
                pyautogui.press("F5")
                pyautogui.sleep(2)
                print("F5")

    cv2.imshow("Image", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
