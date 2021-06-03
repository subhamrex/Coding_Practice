import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img.shape)
img[:] = 255, 25, 255  # whole img coloring ..parition-->200:300:300:200

# 1 width & 2 height..Last params is thickness
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)  # Rectangle
# center point,circle radius,colr scale,thickness
cv2.circle(img, (200, 50), 30, (55, 55, 55), 2)
# After "OpenCV"-> (widhth,height),font name,font size,color scale,thickness
cv2.putText(img, "OpenCV ", (300, 200),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 100, 125), 2)
cv2.imshow("Image", img)


cv2.waitKey(0)
