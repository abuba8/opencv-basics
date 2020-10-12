import cv2

path = 'bosslogic.jpg'
img = cv2.imread(path)
print(img.shape)

width, height = 400, 400
imgResize = cv2.resize(img, (width, height))

imgCrop = img[200:1094, 200:800]

imgCroppedResized = cv2.resize(imgCrop, (img.shape[1], img.shape[0]))

cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)
cv2.imshow("Image Cropped", imgCrop)
cv2.imshow("Image Resized Cropped", imgCroppedResized)

cv2.waitKey(0)