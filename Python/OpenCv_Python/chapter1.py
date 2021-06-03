import cv2
n = int(input("1.Image 2.Video 3.Webcam\n"))
if(n==1):
    print("Loading image...")

    img = cv2.imread("Resources/dog.jpg") #load img
    cv2.imshow("Output", img) #show img
    cv2.waitKey(0) #how much time pic will be shown..0 means always showing
    '''------------------------------------------------------------------'''
elif(n ==2):    
    print("Loading video...")

    cap = cv2.VideoCapture("Resources/ERASED.MP4")

    while True:
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF ==ord('q'): #q to exit video
            break
    '''------------------------------------------------------------------'''    
elif(n==3):  
    print("Using webcam")

    cap =cv2.VideoCapture(0)  
    cap.set(3,640) #set width
    cap.set(4,480) #set height
    cap.set(10,100) #set brightness

    while True:
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF ==ord('q'): #q to exit video
            break
    '''------------------------------------------------------------------'''    
else:
    print("Wrong Input")        
