 import numpy as np
import cv2 as cv
img = np.zeros((512,512,3), np.uint8)
img = cv.rectangle(img, (250,30), (450,200), (100,255,0), 6)
img = cv.circle(img, (100, 400), 20, (255,0,0), 3)
cv.imshow('Draw01',img)
cv.waitKey(0)