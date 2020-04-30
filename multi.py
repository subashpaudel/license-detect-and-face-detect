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


time.sleep(1)
alpr = Alpr("in", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
alpr.set_top_n(20)
dst=os.getcwd()+'\cropedImages'         # destination to save the images
if not os.path.exists(dst):
    os.makedirs(dst)

destination=os.getcwd()+'\Images'         # destination to save the images
if not os.path.exists(destination):
    os.makedirs(destination)







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
##
##            for (x,y,w,h) in faces[i]: 
##        # To draw a rectangle in a face  
##                cv2.rectangle(f,(x,y),(x+w,y+h),(255,255,0),2)  
##                #roi_gray = gray[y:y+h, x:x+w] 
##                roi_color[i] = f[y:y+h, x:x+w]
##                count+=1
##                file=destination+'\\'+str(count)+'.jpg'
##                print(roi_color[i])
##                cv2.imwrite(file,roi_color[i])

            




            
            #print(faces[i])
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
                    # write the image
                    ret[c], enc[c] = cv2.imencode("*.bmp", cropedframe[c])
                    results = alpr.recognize_array(bytes(bytearray(enc[c])))
                    pos_frame = cap[i].get(cv2.CAP_PROP_POS_FRAMES)
                   
                except (IndexError, TypeError) :
                    print("")


            for (x,y,w,h) in faces[i]:
                try:
        # To draw a rectangle in a face  
                    cv2.rectangle(f,(x,y),(x+w,y+h),(255,255,0),2)  
                #roi_gray = gray[y:y+h, x:x+w] 
                    roi_color[i] = f[y:y+h, x:x+w]
                    count+=1
                    file=destination+'\\'+str(count)+'.jpg'
                    
                    cv2.imwrite(file,roi_color[i])

                except (IndexError, TypeError) :   
                    
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
                    
                        newFileWriter.writerow([plateno,cnt, filename, datentime, confidance,window[i],pos_frame]) # write the csv file
                        c=0
                        cntr=0



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
