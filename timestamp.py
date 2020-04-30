import cv2

video_filename = 'car.mp4'

cap = cv2.VideoCapture(video_filename)
print('length = ', cap.get(cv2.CAP_PROP_FRAME_COUNT), '\n')
print('fps = ', cap.get(cv2.CAP_PROP_FPS), '\n')

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

ResultPath = 'output.mp4'

frame_size = (200, 200)   # Final frame size to save video file

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(ResultPath, fourcc, fps = 25.0, frameSize = frame_size)

start = cap.get(cv2.CAP_PROP_POS_MSEC)

##while(cap.isOpened()):
##
##    ret, frame = cap.read()
##
##    if ret==True:
##
##        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##
##        # Detect faces in the image
##        faces = faceCascade.detectMultiScale(
##                gray,
##                scaleFactor=1.1,
##                minNeighbors=5,
##                minSize=(30, 30),
##                )
##
##        # Crop face
##        for (x, y, w, h) in faces:
##            face_frame = frame[y:y+h, x:x+w]
##            face_frame = cv2.resize(face_frame, frame_size)
##
##            # write the face_frame
##            out.write(face_frame)
##
##        cv2.imshow('frame', frame)

if cv2.waitKey(25) & 0xFF == ord('q'):
    
    break



else:
print('Video capture finished')
    end = cap.get(cv2.CAP_PROP_POS_MSEC)
    break

cap.release()
out.release()
cv2.destroyAllWindows()

print('Start time : ', start, '\n')
print('End time : ', end, '\n')
