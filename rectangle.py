import numpy as np
import cv2 as cv
 
img = np.zeros((1150,1550,3), np.uint8)
 
cv.imshow('Draw01',img)
cv.waitKey(0)