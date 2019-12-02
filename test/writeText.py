import numpy
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread('./4.jpg', 1)
cv2.namedWindow('writeText', cv2.WINDOW_NORMAL)
img = cv2.putText(img, 'The text was inserted successfully', (250, 250), font, 4, (0, 0, 255), 3, cv2.LINE_AA)
cv2.imshow('writeText', img)
k = cv2.waitKey(0)
if k == 27:
	img = cv2.resize(img, (950, 660))
	cv2.imwrite('./writeText.jpg', img)
	cv2.destroyAllWindows()