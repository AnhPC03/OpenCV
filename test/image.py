import numpy as np
import cv2
img = cv2.imread('./4.jpg', 1)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
	cv2.destroyAllWindows()
