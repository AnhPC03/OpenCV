import numpy
import cv2

img = cv2.imread('./4.jpg', 1)
cv2.namedWindow('drawCircle', cv2.WINDOW_NORMAL)
img = cv2.circle(img, (500, 500), 300, (0, 255, 0), 4)
cv2.imshow('drawCircle', img)
k = cv2.waitKey(0)
if k == 27:
	img = cv2.resize(img, (950, 660))
	cv2.imwrite('./drawCircle.jpg', img)
	cv2.destroyAllWindows()
