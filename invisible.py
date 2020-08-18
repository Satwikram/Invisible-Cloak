import numpy as np
import cv2
import time

##reading from the webcam
cap = cv2.VideoCapture(0)

time.sleep(3)
count = 0
background = 0

for i in range(60):
    ret, background = cv2.read()

background = np.flip(background, axis = 1)

## Read every frame from the webcam, until the camera is open
while (cap.isOpened()):
    ret, image = cap.read()
    if not ret:
        break
    count = count + 1
    img = np.flip(img, axis=1)

    ## Convert the color space from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## Generat masks to detect red color

