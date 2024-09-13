'''
Simple Cam Test - BGR and Gray
    Create by pythonprogramming.net ==> See the tutorial here:
    https://pythonprogramming.net/loading-video-python-opencv-tutorial
Adapted by Marcelo Rovai - MJRoBot.org @8Feb18
'''


import numpy as np
print("numpy v" + np.__version__) #numpy v2.0.2
import cv2 # ModuleNotFoundError: No module named 'cv2
print("cv2 v" + cv2.__version__)

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1)
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame) # Can't initialize GTK backend in function 'cvInitSystem'
#    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
