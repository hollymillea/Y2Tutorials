import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

path = sys.path[0] + '/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(path)


cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        frame,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    
    for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
            roi_gray = frame[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    # esc
    if key == 27:
        cv2.destroyAllWindows()
        break
    if key == 32:
        cv2.destroyAllWindows()
        break
cap.release()
cv2.destroyAllWindows()