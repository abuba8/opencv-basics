import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

#img[:] = 255, 0, 0
#last parameter thickness in line and rec, second last color
cv2.line(img, (0,0),(img.shape[1], img.shape[0]), (0,255,0), 2)
cv2.rectangle(img,(350,100), (450,200), (0,0,255), cv2.FILLED)
cv2.circle(img, (150, 400), 50, (255,0,0), 2)
cv2.putText(img, "Testing, how to draw shape and write text", (75,50), cv2.FONT_HERSHEY_PLAIN, 1, (0,150,0), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)