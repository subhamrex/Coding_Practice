import cv2
import numpy as np

img = cv2.imread("Resources/dog.jpg")
print(img.shape)

imgResize = cv2.resize(img,(500,600)) #(Width,Height)--> Resize img
print(imgResize.shape)

imgCropped = img[0:200,200:500] #here height comes first

cv2.imshow("Output", imgResize) #show img
cv2.imshow("Cropped img: ",imgCropped)
cv2.waitKey(0)