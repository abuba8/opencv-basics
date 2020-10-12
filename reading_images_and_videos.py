import cv2


'''images
img = cv2.imread("bosslogic.jpg")
cv2.imshow("KB", img)

cv2.waitKey(0)

'''


'''videoes
frameWidth = 640
frameHeight = 360

cap = cv2.VideoCapture(0)
#cap.set(3, frameWidth)
#cap.set(4, frameHeight)

while True:
	s, img = cap.read()
	img = cv2.resize(img,(frameWidth, frameHeight))
	cv2.imshow("Webcam", img)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
'''