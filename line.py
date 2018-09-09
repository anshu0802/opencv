import numpy as np
import cv2 as cv
 
img = np.zeros((512,512,3), np.uint8)
 
#draw a red line
img = cv.line(img, (100,100), (300,300), (0,0,255),4)
 
cv.imshow('Draw01',img)
cv.waitKey(0)