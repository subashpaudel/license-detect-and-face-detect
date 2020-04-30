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

name=['car.mp4','car1.mp4']
window=['cam1','cam2']
cap = [cv2.VideoCapture(i) for i in name]
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







fieldnames = [ 'Plate number','ID', 'Image Path','Date and time ' ,'Confidance','window']
fileID=open('file.csv','w')       # file to save the data
newFileWriter = csv.writer(fileID)
newFileWriter.writerow(fieldnames)
print("Using OpenALPR " + alpr.get_version())





       






bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500, detectShadows=False)

print ('Training BG Subtractor-')

frames = [None] * len(name)
faces = [None] * len(name)
gray = [None] * len(name)
ret = [None] * len(name)
Rfilter= [None] * len(name)
filtered=[None] * len(name)
edged=[None] * len(name)
fg_mask=[None] * len(name)
enc=[None] * len(name)
cropedframe=[None] * len(name)
roi_color=[None] * len(name)
x=[None] * len(name)
y=[None] * len(name)
h=[None] * len(name)
w=[None] * len(name)
cnt=0
count=0
while True:

    for i,c in enumerate(cap):
        if c is not None:
            ret[i], frames[i] = c.read()
    for i,f in enumerate(frames):
        #s=True
        if ret[i] is True :
            #print(type(ret[i]))
            gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
            Rfilter[i] = cv2.bilateralFilter(gray[i], 5, 70, 70)
            faces[i]=face_cascade.detectMultiScale(gray[i], 1.3, 5)

            for c in range(0, len(faces[i])):
                try:
                    cv2.rectangle(f, (x[c], y[c]), (x[c] + w[c] - 1, y[c] + h[c] - 1),(255, 255, 0), 1)
                    roi_color[c]=f[y[c]:y[c]+h[c], x[c]:x[c]+w[c]]

                    
                    count+=1
                    file=destination+'\\'+str(count)+'.jpg'
                    print(roi_color[c])
                    cv2.imwrite(file,roi_color[c])
                except(IndexError,TypeError):
                    print("")


            
           # print(faces[i])
##
            ##                     
##                     
                     


            ##        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            ret[i], filtered[i] = cv2.threshold(Rfilter[i], 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            filtered[i] = cv2.medianBlur(f, 5)
            edged[i] = cv2.Canny(gray[i], 50, 50)
            fg_mask[i] = bg_subtractor.apply(filtered[i], None, 0.01)
            cv2.imshow(window[i], gray[i])
            contours, hierarchy = cv2.findContours(fg_mask[i], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            #cnt=0
            
            cntr = []
    
            for contour in contours:
                contourSize = cv2.contourArea(contour)
                if (contourSize > 10000):

                    cntr.append(contour)
                    #print(cntr)
                    cnt+=1
            #cnt=0
            #print(len(cntr))
            for c in range(0, len(cntr)):
                
                #print(cntr)
                #cntr = [None] * len[name]
                #cntr.append(ii)
                try:
                    (x[c], y[c], w[c], h[c]) = cv2.boundingRect(cntr[c])
                #print(cv2.boundingRect(cntr[c]))
                    cv2.rectangle(f, (x[c], y[c]), (x[c] + w[c] - 1, y[c] + h[c] - 1),(255, 255, 0), 1)
                    cropedframe[c]=f[y[c]:y[c]+h[c], x[c]:x[c]+w[c]]

                    
                     
                    filename=dst+'\\'+str(cnt)+'.jpg'
                    cv2.imwrite(filename,cropedframe[c])
##          ##                
                    # write the image
                    ret[c], enc[c] = cv2.imencode("*.bmp", cropedframe[c])
                    file=destination+'\\'+str(count)+'.jpg'
                    results = alpr.recognize_array(bytes(bytearray(enc[c])))
                    
                    pos_frame = cap[i].get(cv2.CAP_PROP_POS_FRAMES)
                    
                
                    

                except(IndexError, TypeError):
                    
                      
                      
                      
                            
            

                     
                    
                    if results['results']:


                
                        print('License plate Detected and Recorded')
                
                        datentime = time.asctime( time.localtime(time.time()) )
                #time =  datetime.datetime.now().time() 
                #date = datetime.datetime.now().date()
                        plateno = results['results'][0]['plate']
                        confidance=results['results'][0]['confidence']
                        #window=results['results'][0]['window']
                
                        print('Plate: ',plateno, 'Confidance: ',confidance,'Window: ',window[i],'Frame_no:',str(pos_frame),)
                        print("\n")
                            
                           
            
                        newFileWriter.writerow([plateno,cnt, filename, datentime, confidance,window[i],pos_frame,file]) # write the csv file
                        c=0
                        cntr=0
                        face=0



    if cv2.waitKey(3) ==27:
       break
    if cap[i].get(cv2.CAP_PROP_POS_FRAMES) == cap[i].get(cv2.CAP_PROP_FRAME_COUNT):
                        # If the number of captured frames is equal to the total number of frames,
                        # we stop
                        break

    
    

#print("cuurent running",window[0])
#print("cuurent running",window[1])
for c in cap:
    if c is not None:
        c.release()

cv2.destroyAllWindows()























      
##cam = cv2.VideoCapture('car.mp4')
###cap=cv2.VideoCapture('car.mp4')
###cv2.namedWindow("test")
##time.sleep(1)
##alpr = Alpr("in", "openalpr.conf", "runtime_data")
##if not alpr.is_loaded():
##    print("Error loading OpenALPR")
##    sys.exit(1)
##    
##alpr.set_top_n(20)
##dst=os.getcwd()+'\cropedImages'         # destination to save the images
##if not os.path.exists(dst):
##    os.makedirs(dst)
##
##fieldnames = ['ID', 'Plate number', 'Image Path','Date and time ' ,'Confidance']
##fileID=open('file.csv','w')       # file to save the data
##newFileWriter = csv.writer(fileID)
##newFileWriter.writerow(fieldnames)
#####alpr = Alpr("us","C:/Users/sawankashyap/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/openalpr/openalpr.conf" , "C:/Users/sawankashyap/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/openalpr/runtime_data")
#####alpr = Alpr("mx", "C:/openALPR_1/openalpr_64/openalpr.conf", "C:/openALPR_1/openalpr_64/runtime_data")
#####alpr.set_top_n(10)
####alpr.set_default_region("md")
####if not alpr.is_loaded():
####    sys.exit(1)
####
##print("Using OpenALPR " + alpr.get_version())
#####cap = cv2.VideoCapture("C:/Users/sawankashyap/Downloads/ALPR--Automatic-License-Plate-Recognition-master/ALPR--Automatic-License-Plate-Recognition-master/15ene2018")
##bg_subtractor = cv2.createBackgroundSubtractorMOG2(
##    history=500, detectShadows=False)
##
##print ('Training BG Subtractor-')
##cv2.namedWindow('op', cv2.WINDOW_NORMAL)
##cnt=0
##while True:
##    ok,frame=cam.read()
##    if not ok:
##        sys.exit()
##    else:
##        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
##        Rfilter = cv2.bilateralFilter(gray, 5, 70, 70)
##
####        # Threshold image
##        ret, filtered = cv2.threshold(Rfilter, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
##        filtered = cv2.medianBlur(frame, 5)
##        edged = cv2.Canny(gray, 50, 50)
##        fg_mask = bg_subtractor.apply(filtered, None, 0.01)
##        #fg_mask = filter_mask(fg_mask)
##        contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
##
##        cntr = []
##        for contour in contours:
##            contourSize = cv2.contourArea(contour)
##            if (contourSize > 10000):
##                cntr.append(contour)
##                cnt+=1
####
##        for ii in range(0, len(cntr)):
##            (x, y, w, h) = cv2.boundingRect(cntr[ii])
##            cv2.rectangle(frame, (x, y), (x + w - 1, y + h - 1),(255, 255, 0), 1)
##            cropedframe=frame[y:y+h, x:x+w]
##            filename=dst+'\\'+str(cnt)+'.jpg'
##            cv2.imwrite(filename,cropedframe) # write the image
##            ret, enc = cv2.imencode("*.bmp", cropedframe)
##            results = alpr.recognize_array(bytes(bytearray(enc)))
##            if results['results']:
##                
##                print('License plate Detected and Recorded')
##                
##                datentime = time.asctime( time.localtime(time.time()) )
##                #time =  datetime.datetime.now().time() 
##                #date = datetime.datetime.now().date()
##                plateno = results['results'][0]['plate']
##                confidance=results['results'][0]['confidence']
##                
##                print('Plate: ',plateno, 'Confidance: ',confidance)
##                print("\n")
##                newFileWriter.writerow([cnt, str(plateno), filename, datentime, str(confidance)]) # write the csv file
##
##        cv2.imshow('op', frame)
##        if cv2.waitKey(33) == 27:
##            break
##        
        

