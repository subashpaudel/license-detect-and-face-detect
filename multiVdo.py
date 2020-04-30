from openalpr import Alpr
import cv2
import sys
import os
import time
import csv
from datetime import datetime
#from filter
##cam = cv2.VideoCapture('car.mp4')
##cam2 = cv2.VideoCapture('car1.mp4')
###cam3=cv2.VideoCapture('15ene2018.avi')
##if(cam.isOpened()==False):
##    print("error opening the cam file")
##if(cam2.isOpened()==False):
##    print("error opening the cam2 file ")
####if(cam3.isOpened()==False):
####    print("error opening the cam3 file ")
###while (cam.isOpened() or cam2.isOpened() or cam.isOpened() ):
##alpr = Alpr("in", "openalpr.conf", "runtime_data")
##if not alpr.is_loaded():
##    print("Error loading OpenALPR")
##    sys.exit(1)
##    
##alpr.set_top_n(20)
##dst=os.getcwd()+'\cropedImages'         # destination to save the images
##if not os.path.exists(dst):
##    os.makedirs(dst)
##if (cam is True):
##    
##    fieldnames = ['ID', 'Plate number', 'Image Path','Date and time ' ,'Confidance']
##    fileID=open('file1.csv','w')       # file to save the data
##    newFileWriter = csv.writer(fileID)
##    newFileWriter.writerow(fieldnames)
###alpr = Alpr("us","C:/Users/sawankashyap/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/openalpr/openalpr.conf" , "C:/Users/sawankashyap/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/openalpr/runtime_data")
###alpr = Alpr("mx", "C:/openALPR_1/openalpr_64/openalpr.conf", "C:/openALPR_1/openalpr_64/runtime_data")
###alpr.set_top_n(10)
##    alpr.set_default_region("md")
##    if not alpr.is_loaded():
##        sys.exit(1)
##
##    print("Using OpenALPR " + alpr.get_version())
###cap = cv2.VideoCapture("C:/Users/sawankashyap/Downloads/ALPR--Automatic-License-Plate-Recognition-master/ALPR--Automatic-License-Plate-Recognition-master/15ene2018")
##    bg_subtractor = cv2.createBackgroundSubtractorMOG2(
##    history=500, detectShadows=False)
##
##    print ('Training BG Subtractor-')
##    cv2.namedWindow('op', cv2.WINDOW_NORMAL)
##    cnt=0
##    while True:
##        ok,frame=cam.read()
##        if not ok:
##            sys.exit()
##        else:
##            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
##            Rfilter = cv2.bilateralFilter(gray, 5, 70, 70)
##
##        # Threshold image
##            ret, filtered = cv2.threshold(Rfilter, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
##            filtered = cv2.medianBlur(frame, 5)
##            edged = cv2.Canny(gray, 50, 50)
##            fg_mask = bg_subtractor.apply(filtered, None, 0.01)
##        #fg_mask = filter_mask(fg_mask)
##            contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
##
##            cntr = []
##            for contour in contours:
##                contourSize = cv2.contourArea(contour)
##                if (contourSize > 10000):
##                    cntr.append(contour)
##                    cnt+=1
##
##            for ii in range(0, len(cntr)):
##                (x, y, w, h) = cv2.boundingRect(cntr[ii])
##                cv2.rectangle(frame, (x, y), (x + w - 1, y + h - 1),(255, 255, 0), 1)
##                cropedframe=frame[y:y+h, x:x+w]
##                filename=dst+'\\'+str(cnt)+'.jpg'
##                cv2.imwrite(filename,cropedframe) # write the image
##                ret, enc = cv2.imencode("*.bmp", cropedframe)
##                results = alpr.recognize_array(bytes(bytearray(enc)))
##                if results['results']:
##                
##                    print('License plate Detected and Recorded')
##                
##                    datentime = time.asctime( time.localtime(time.time()) )
##                #time =  datetime.datetime.now().time() 
##                #date = datetime.datetime.now().date()
##                    plateno = results['results'][0]['plate']
##                    confidance=results['results'][0]['confidence']
##                
##                    print('Plate: ',plateno, 'Confidance: ',confidance)
##                    print("\n")
##                    newFileWriter.writerow([cnt, str(plateno), filename, datentime, str(confidance)]) # write the csv file
##
##            cv2.imshow('op', frame)
##            
##if (cam2):
##                
##    fieldnames2 = ['ID', 'Plate number', 'Image Path','Date and time ' ,'Confidance']
##    fileID2=open('file2.csv','w')       # file to save the data
##    newFileWriter2 = csv.writer(fileID2)
##    newFileWriter2.writerow(fieldnames2)
###alpr = Alpr("us","C:/Users/sawankashyap/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/openalpr/openalpr.conf" , "C:/Users/sawankashyap/AppData/Local/Programs/Python/Python36-32/Lib/site-packages/openalpr/runtime_data")
###alpr = Alpr("mx", "C:/openALPR_1/openalpr_64/openalpr.conf", "C:/openALPR_1/openalpr_64/runtime_data")
###alpr.set_top_n(10)
##    alpr.set_default_region("md")
##    if not alpr.is_loaded():
##        
##        sys.exit(1)
##
##    print("Using OpenALPR " + alpr.get_version())
###cap = cv2.VideoCapture("C:/Users/sawankashyap/Downloads/ALPR--Automatic-License-Plate-Recognition-master/ALPR--Automatic-License-Plate-Recognition-master/15ene2018")
##    bg_subtractor2 = cv2.createBackgroundSubtractorMOG2(
##                history=500, detectShadows=False)
##
##    print ('Training BG Subtractor-')
##    cv2.namedWindow('op2', cv2.WINDOW_NORMAL)
##    cnt2=0
##    while True:
##        
##        ok2,frame2=cam2.read()
##        if not ok2:
##            sys.exit()
##        else:
##            
##            gray = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)
##            Rfilter = cv2.bilateralFilter(gray, 5, 70, 70)
##
##        # Threshold image
##            ret2, filtered2 = cv2.threshold(Rfilter, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
##            filtered2 = cv2.medianBlur(frame2, 5)
##            edged2 = cv2.Canny(gray, 50, 50)
##            fg_mask2 = bg_subtractor2.apply(filtered2, None, 0.01)
##        #fg_mask = filter_mask(fg_mask)
##            contours2, hierarchy = cv2.findContours(fg_mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
##
##            cntr2 = []
##            for contour2 in contours2:
##                contourSize2 = cv2.contourArea(contour2)
##                if (contourSize2 > 10000):
##                    
##                    cntr2.append(contour2)
##                    
##                    cnt2+=1
##
##            for ii in range(0, len(cntr2)):
##                (x, y, w, h) = cv2.boundingRect(cntr2[ii])
##
##                cv2.rectangle(frame2, (x, y), (x + w - 1, y + h - 1),(255, 255, 0), 1)
##                cropedframe2=frame2[y:y+h, x:x+w]
##                filename2=dst+'\\'+str(cnt2)+'.jpg'
##                cv2.imwrite(filename2,cropedframe2) # write the image
##                ret2, enc2 = cv2.imencode("*.bmp", cropedframe2)
##                results2 = alpr.recognize_array(bytes(bytearray(enc2)))
##                if results2['results']:
##                
##                    print('License plate Detected and Recorded')
##                
##                    datentime2 = time.asctime( time.localtime(time.time()) )
##                #time =  datetime.datetime.now().time() 
##                #date = datetime.datetime.now().date()
##                    plateno2 = results2['results'][0]['plate']
##                    confidance2=results2['results'][0]['confidence']
##                
##                    print('Plate: ',plateno2, 'Confidance: ',confidance2)
##                    print("\n")
##                    newFileWriter2.writerow([cnt2, str(plateno2), filename2, datentime2, str(confidance2)]) # write the csv file
##
##                cv2.imshow('op2', frame2)
##                    
##                    
##                if cv2.waitKey(33) & 0xFF == ('q'):
##                        
##                    break
##cam.release()
##cam2.release()
##cv2.destroyAllWindows()
##        




alpr = Alpr("in", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
alpr.set_top_n(20)
dst=os.getcwd()+'\cropedImages'         # destination to save the images
if not os.path.exists(dst):
    os.makedirs(dst)

 

fieldnames = ['ID', 'Plate number', 'Image Path','Date and time ' ,'Confidance']
fileID=open('file.csv','w')       # file to save the data
newFileWriter = csv.writer(fileID)
newFileWriter.writerow(fieldnames)
print("Using OpenALPR " + alpr.get_version())

 

name=['car.mp4','car1.mp4','15ene2018.avi']
window=['op1','op2','op3']
cap = [cv2.VideoCapture(i) for i in name]
time.sleep(1)

 

bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500, detectShadows=False)

 

print ('Training BG Subtractor-')

 

frames = [None] * len(name)
gray = [None] * len(name)
ret = [None] * len(name)
Rfilter= [None] * len(name)
filtered=[None] * len(name)
edged=[None] * len(name)
fg_mask=[None] * len(name)
enc=[None] * len(name)
cropedframe=[None] * len(name)
x=[None] * len(name)
y=[None] * len(name)
h=[None] * len(name)
w=[None] * len(name)
cnt=0
while True:

 

    for i,c in enumerate(cap):
        if c is not None:
            ret[i], frames[i] = c.read()
    for i,f in enumerate(frames):
        #s=True
        if ret[i] is True :
            #print(type(ret[i]))
            gray[i] = cv2.cvtColor(f, cv2.COLOR_RGB2GRAY)
            Rfilter[i] = cv2.bilateralFilter(gray[i], 5, 70, 70)
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
                try:
                #print(cntr)
                #cntr = [None] * len[name]
                #cntr.append(ii)
                (x[c], y[c], w[c], h[c]) = cv2.boundingRect(cntr[c])
                #print(cv2.boundingRect(cntr[c]))
                cv2.rectangle(f, (x[c], y[c]), (x[c] + w[c] - 1, y[c] + h[c] - 1),(255, 255, 0), 1)
                cropedframe[c]=f[y[c]:y[c]+h[c], x[c]:x[c]+w[c]]
                filename=dst+'\\'+str(cnt)+'.jpg'
                cv2.imwrite(filename,cropedframe[c]) # write the image
                ret[c], enc[c] = cv2.imencode("*.bmp", cropedframe[c])
                results = alpr.recognize_array(bytes(bytearray(enc[c])))
                except IndexError:
                    continue
                if results['results']:
                
                    print('License plate Detected and Recorded')
                
                    datentime = time.asctime( time.localtime(time.time()) )
                #time =  datetime.datetime.now().time() 
                #date = datetime.datetime.now().date()
                    plateno = results['results'][0]['plate']
                    confidance=results['results'][0]['confidence']
                
                    print('Plate: ',plateno, 'Confidance: ',confidance)
                    print("\n")
                    newFileWriter.writerow([cnt, str(plateno), filename, datentime, str(confidance)]) # write the csv file
                    c=0
                    cntr=0

 

 

    if cv2.waitKey(33) == 27:
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
        

