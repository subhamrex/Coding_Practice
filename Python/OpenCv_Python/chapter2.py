import cv2
import numpy as np

img = cv2.imread("Resources/dog.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Covert img rgb to gray scale

imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # blur img

imgCanny = cv2.Canny(img, 100, 100) #get edges

imgDilation = cv2.dilate(imgCanny,kernel,iterations=1) #after increasing iteration we will see massive thickness

imgEroded = cv2.erode(imgDilation,kernel,iterations=1) #erode img

cv2.imshow("Gray img:", imgGray)
cv2.imshow("Blur img:", imgBlur)
cv2.imshow("Canny img:", imgCanny)
cv2.imshow("Dilation img:", imgDilation)
cv2.imshow("Erode img:", imgEroded)


cv2.waitKey(0)
