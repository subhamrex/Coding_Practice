import cv2

def motion_detection(draw=True):        
    initial_static_back = None
    video_object = cv2.VideoCapture(0)
    print ("#"*100)
    print ("                        Initialized video capture")
    print ("#"*100)
    """ Run application on infinity loop"""
    while True:
        check, live_frame = video_object.read()
        is_motion_detected = 0
        gray = cv2.cvtColor(live_frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if initial_static_back is None:
            initial_static_back = gray
            continue
        # Difference frame will display the difference between initial frame and current live frame
        difference_frame = cv2.absdiff(initial_static_back, gray)
        
        ## This code block will display the threshold between the frames
        threshold_frame = cv2.threshold(difference_frame, 30, 255, cv2.THRESH_BINARY)[1]
        threshold_frame = cv2.dilate(threshold_frame, None, iterations = 2)
        cnts, hierarchy = cv2.findContours(threshold_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        # Code block for identifying the differences between the frames and draw the rectangle for the frame difference aria
        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            is_motion_detected = 1
            # print (">>>>> Motion detected")
            (x, y, w, h) = cv2.boundingRect(contour)
            # Draw the rectangle in yellow color for identified area/ differences
            if draw:
                cv2.rectangle(live_frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
            cv2.putText(live_frame, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
        
        # Display/ render video different frames for development
        #cv2.imshow("Gray Frame", gray)
        #cv2.imshow("Difference Frame", difference_frame)
        #cv2.imshow("Threshold Frame", threshold_frame)
        cv2.imshow("Color Frame", live_frame)
        # Quit/ exit the execution if we press 'e' or 'q' key on the keyboard
        key = cv2.waitKey(1)
        if key == ord('e') or key == ord('q'):
            break
    # release video control
    video_object.release()
    # Destroying and closing all windows 
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    motion_detection()