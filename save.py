import numpy as np
import cv2
img=cv2.imread('/Users/anshurathour/Desktop/image.png', -1)
img=cv2.imwrite('/Users/anshurathour/Desktop/image.jpg',img)
cv2.imshow('Orignal',img)
cv2.waitKey(0)
cv2.destroyAllWindows()