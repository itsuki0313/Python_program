#config : UTF-8

import numpy as np
import cv2

img = cv2.imread('lena.jpg',0)

cv2.imshow('lena',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
