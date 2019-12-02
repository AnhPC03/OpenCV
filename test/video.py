import cv2

vid = cv2.VideoCapture('./video.mp4')

count = 0
success = 1

while(success):
	success, img = vid.read()
	if count % 20 == 0:
		if success:
			cv2.imwrite('frame_%d.jpg' % count, img)
	count += 1

vid.release()
cv2.destroyAllWindows()
