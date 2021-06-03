import cv2
import numpy as np

img = cv2.imread("Resources/trump.jpg")  # load img

width, height = 250, 350
pts1 = np.float32([[227, 93],  [430, 136], [162, 379],[
                  370, 426]])  # left top,right top,left bottom,right bottom
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2) #Transformation
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)  # show img
cv2.imshow("Output Img:", imgOutput)
cv2.waitKey(0)
