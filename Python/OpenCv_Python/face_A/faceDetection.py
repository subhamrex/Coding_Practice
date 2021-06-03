import cv2
from face_recognition.api import face_locations
import numpy as np
import face_recognition

img = face_recognition.load_image_file('Img/Ali.jpg')
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Img/AliTest.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

face_loc = face_recognition.face_locations(img)[0]
encoderImg = face_recognition.face_encodings(img)[0]
cv2.rectangle(img,(face_loc[3],face_loc[0]),(face_loc[1],face_loc[2]),(255,0,255),2)

face_locTest = face_recognition.face_locations(imgTest)[0]
encoderImgTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(face_locTest[3],face_locTest[0]),(face_locTest[1],face_locTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encoderImg],encoderImgTest)
faceDis = face_recognition.face_distance([encoderImg],encoderImgTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('Identity',img)
cv2.imshow('Test',imgTest)
cv2.waitKey(0)
