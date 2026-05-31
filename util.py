import numpy as np 
import cv2
def get_limits(color):
    c= np.uint8([[color]])
    hsvC = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    hue = hsvC[0][0][0]
    lowerLimit = np.array([max(hue - 10, 0), 100, 100], dtype=np.uint8)
    upperLimit = np.array([min(hue + 10, 179), 255, 255], dtype=np.uint8)

     
    return lowerLimit, upperLimit
