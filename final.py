import cv2

def frame_capture():
        cap = cv2.VideoCapture("car.mp4")
        while not cap.isOpened():
                cap = cv2.VideoCapture("car.mp4")
                cv2.waitKey(1000)
                print ("Wait for the header")

        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        while True:
                
                flag, frame = cap.read()
                if flag:
                        
                        
                        cv2.imshow("video", frame)
                        # The frame is ready and already captured
                        #cv2.imshow('video', frame)
                        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                        print (str(pos_frame)+" frames")
                else:
                        # The next frame is not ready, so we try to read it again
                        cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
                        print ("frame is not ready")
                        # It is better to wait for a while for the next frame to be ready
                        cv2.waitKey(1000)

                if cv2.waitKey(10) == 27:
                        break
                if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                        # If the number of captured frames is equal to the total number of frames,
                        # we stop
                        break
frame_capture()
