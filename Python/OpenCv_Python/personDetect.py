import cv2

#cap = cv2.VideoCapture(0) # For Webcam
cap = cv2.VideoCapture("Resources/demo.mp4") #video
   
    
pedestrian_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_fullbody.xml") 

while True:
    # reads frames from a video
    ret, frames = cap.read()
    # convert to gray scale of each frames
    #gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    # Detects pedestrians of different sizes in the input image
    pedestrians = pedestrian_cascade.detectMultiScale( frames, 1.1, 
    1)
    # To draw a rectangle in each pedestrians
    for (x,y,w,h) in pedestrians:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,255,0),2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frames, 'Person', (x + 6, y - 6), font, 0.5, (0, 
        255, 0), 1)
        # Display frames in a window
    cv2.imshow('Pedestrian detection', frames)
    # Wait for Enter key to stop
    if cv2.waitKey(33) == 13:
        break   
    

cap.release()
cv2.destroyAllWindows()   