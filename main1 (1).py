from openalpr import Alpr
import cv2
import sys
import os
import time
import csv
from datetime import datetime
import random
#from filter

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture('car.mp4')







#cv2.namedWindow("test")
time.sleep(1)
alpr = Alpr("in", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
    
alpr.set_top_n(20)


destination=os.getcwd()+'\Images'         # destination to save the images
if not os.path.exists(destination):
    os.makedirs(destination)


dst=os.getcwd()+'\cropedImages'         # destination to save the images
if not os.path.exists(dst):
    os.makedirs(dst)




fieldnames = ['Plate number','ID', 'Image Path','Date and time ' ,'Confidance','Frame_no','face path']
fileID=open('file.csv','w')       # file to save the data
newFileWriter = csv.writer(fileID)
newFileWriter.writerow(fieldnames)
#alpr = Alpr("us","C:/Users/sawankashyap/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/openalpr/openalpr.conf" , "C:/Users/sawankashyap/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/openalpr/runtime_data")
#alpr = Alpr("mx", "C:/openALPR_1/openalpr_64/openalpr.conf", "C:/openALPR_1/openalpr_64/runtime_data")
#alpr.set_top_n(10)
alpr.set_default_region("md")
if not alpr.is_loaded():
    sys.exit(1)

print("Using OpenALPR " + alpr.get_version())
#cap = cv2.VideoCapture("C:/Users/sawankashyap/Downloads/ALPR--Automatic-License-Plate-Recognition-master/ALPR--Automatic-License-Plate-Recognition-master/15ene2018")
bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500, detectShadows=False)

print ('Training BG Subtractor...')
cv2.namedWindow('op', cv2.WINDOW_NORMAL)
count=0
cnt=0
while True:
    ok,frame=cam.read()
    if not ok:
        sys.exit()
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        Rfilter = cv2.bilateralFilter(gray, 5, 70, 70)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces: 
        # To draw a rectangle in a face  
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)  
            roi_gray = gray[y:y+h, x:x+w] 
            roi_color = frame[y:y+h, x:x+w]
            count+=1
            file=destination+'\\'+str(count)+'.jpg'
            cv2.imwrite(file,roi_color)
            print(roi_color)
          


        
            

        # Threshold image
        ret, filtered = cv2.threshold(Rfilter, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        filtered = cv2.medianBlur(frame, 5)
        edged = cv2.Canny(gray, 50, 50)
        fg_mask = bg_subtractor.apply(filtered, None, 0.01)
        #fg_mask = filter_mask(fg_mask)
        contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        cntr = []
        for contour in contours:
            contourSize = cv2.contourArea(contour)
            if (contourSize > 10000):
                cntr.append(contour)
                cnt+=1

        for ii in range(0, len(cntr)):
            (x, y, w, h) = cv2.boundingRect(cntr[ii])
            cv2.rectangle(frame, (x, y), (x + w , y + h ),(255, 255, 0), 2)
            roi_gra = gray[y:y+h, x:x+w] 
            cropedframe=frame[y:y+h, x:x+w]
            filename=dst+'\\'+str(cnt)+'.jpg'
            cv2.imwrite(filename,cropedframe) # write the image
            ret, enc = cv2.imencode("*.bmp", cropedframe)
            file=destination+'\\'+str(count)+'.jpg'
         
            
            
            
            results = alpr.recognize_array(bytes(bytearray(enc)))


        
            

        
            
            



            pos_frame = cam.get(cv2.CAP_PROP_POS_FRAMES)
##            while True:
##                
##                flag, frame = cam.read()
##                if flag:
##                        
##        
##                        # The frame is ready and already captured
##                        #cv2.imshow('video', frame)
##                    pos_frame = cam.get(cv2.CAP_PROP_POS_FRAMES)
####                        print (str(pos_frame)+" frames")
##            
            start = cam.get(cv2.CAP_PROP_POS_MSEC)/1000
            
            
            #tt=cam.get(cv2.CAP_PROP_POS_AVI_RATIO)
            #s=(start/1000)%60
            #seconds=float(s)

##            start_time = time.time()
##            timeElapsed = start_time - time.time() 
##            secElapsed = int(timeElapsed)
            #timestamp=cam.set(cv2.CAP_PROP_POS_MSEC,start)
          
            if results['results']:
                print('License plate Detected and Recorded')
                print("\n")
                
                datentime = time.asctime( time.localtime(time.time()) )
                    
                
                #time =  datetime.datetime.now().time() 
                #date = datetime.datetime.now().date()
                plateno = results['results'][0]['plate']
                confidance=results['results'][0]['confidence']
                
                
                print('Plate: ',plateno, 'Confidance: ',confidance,'Starttime: ',start,'Frame:',str(pos_frame))
                newFileWriter.writerow([ str(plateno),cnt, filename, datentime, str(confidance),str(pos_frame),file])

##                with open('file.csv', 'r') as csvFile:
##                    reader = csv.reader(csvFile)
##                    for row in reader:
##                        print(row)
                    
    
    
        

                # write the csv file

                
                    
                    
                

        cv2.imshow('op', frame)
        if cv2.waitKey(33) == 27:
            break
        if cam.get(cv2.CAP_PROP_POS_FRAMES) == cam.get(cv2.CAP_PROP_FRAME_COUNT):
                        # If the number of captured frames is equal to the total number of frames,
                        # we stop
                        break


        #end = cam.get(cv2.CAP_PROP_POS_MSEC)
        #print('End time : ', end, '\n')
       # print('Video capture finished')
        
            

##cam.release()

##print('Start time : ', start+5000, '\n')
##print('End time : ', end+5000, '\n')

        

        
        

