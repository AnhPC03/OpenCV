import numpy
import cv2

img = cv2.imread('./4.jpg', 1)
cv2.namedWindow('drawRectangle', cv2.WINDOW_NORMAL)
img = cv2.rectangle(img, (150, 150), (350, 450), (0, 0, 255), 4)
cv2.imshow('drawRectangle', img)
k = cv2.waitKey(0)
if k == 27:
	img = cv2.resize(img, (950, 660))
	cv2.imwrite('./drawRectangle.jpg', img)
	cv2.destroyAllWindows()