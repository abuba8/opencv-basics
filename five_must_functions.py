import cv2
import numpy as np

path = 'bosslogic.jpg'
kernel = np.ones((5,5), np.uint8)

#normal
img = cv2.imread(path)

#grayscale first 
#img = cv2.imread(path, 0)

#grayscale second
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#blur image
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)

#edge detection
imgCanny = cv2.Canny(imgBlur, 100, 100)

#dilation
imgDilation = cv2.dilate(imgCanny,kernel, iterations = 1)

#erosion
imgErosion = cv2.erode(imgDilation, kernel, iterations = 1)

#cv2.imshow("Image", img)
#cv2.imshow("Gray Scale", imgGray)
#cv2.imshow("Image Blur", imgBlur)
#cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Dilation", imgDilation)
cv2.imshow("Image Erosion", imgErosion)




cv2.waitKey(0)