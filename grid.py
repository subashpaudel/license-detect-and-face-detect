from tkinter import *
from PIL import ImageTk,Image
import csv
from tkinter import messagebox
from tkinter import ttk
from tkinter import Frame
import tkinter as tk
import cv2
#from tkMessageBox import *

master=Tk()
master.title("Automatic license plate Recognition")
master.geometry("900x900")
##
##white 		= "#ffffff"
##lightBlue2 	= "#adc5ed"
##font 		= "Constantia"
##fontButtons = (font, 12)
##maxWidth  	= 800
##maxHeight 	= 480
##
##
##
###Graphics window
##mainWindow = tk.Tk()
##mainWindow.configure(bg=lightBlue2)
##mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))
##mainWindow.resizable(0,0)
### mainWindow.overrideredirect(1)
####
##mainFrame = Frame(master)
##mainFrame.place(x=20, y=20)                
##
###Capture video frames
##lmain = Label(master)
##lmain.grid(sticky=E+W)

frameno=0




label1=Label(master,text="Plate No:", font=(None, 10))
label2=Label(master,text="Count:", font=(None, 10),height=5)
label3=Label(master,text="Date and Time :", font=(None, 10), height=5)
label4=Label(master,text="Accuracy:", font=(None, 10), height=5)
#label5=Label(master,text="Choose Camera:", font=(None, 10), height=5)
label6=Label(master,text="Camera number:",font=(None, 10), height=5)





label1.grid(sticky=E+W)
label2.grid(sticky=E+W)
label3.grid(sticky=E+W)
label4.grid(sticky=E+W)
#label5.grid(sticky=E+W)
label6.grid(sticky=E+W)




v1=StringVar()
entry1=Entry(master,textvariable=v1)
v2=StringVar()
entry2=Entry(master,textvariable=v2)
v3=StringVar()
entry3=Entry(master,textvariable=v3)
v4=StringVar()
entry4=Entry(master,textvariable=v4)
v5=StringVar()
entry5=Entry(master,textvariable=v5)




##v7=StringVar()
######
##drop = OptionMenu(master,v7,'cam1','cam2')
######
##drop.grid(row=4, column=1)




entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)



#search button
urlInput = StringVar()
inputUser = Entry(master, textvariable=urlInput)
inputUser.grid(columnspan=2, sticky=W)


image1=Label(master)
image1.grid(row=0, column=2, columnspan=2, rowspan=4,
               sticky=W+E+N+S, padx=5, pady=5)


def get_me():

    column_values = set()
    new_rows = []
    
    first_time_line = None

    with open('file.csv','r') as csvfile:
        datareader = csv.reader(csvfile)
        for line, row in enumerate(datareader):
            try:
                first_column = row[0]
                #second_column = row[5]
            except IndexError:
                continue
            else:
            
                
                if first_column.strip() == urlInput.get():
                    

                    #column_values.add(row[5])
                    new_rows.append(row[5])
                    mylist = list(dict.fromkeys(new_rows))
                    
                    

                    v1.set(row[0])
                    v2.set(row[1])
                    v3.set(row[3])
                    v4.set(row[4])
                    v5.set(mylist)
                    
                    
                    global frameno
                    frameno=int(float(row[6]))
                    
                    
                    

                  
                    path=row[2]

                    
                    logo1=Image.open(path)

                    resized1=logo1.resize((400,400),Image.ANTIALIAS)
                    logo3=ImageTk.PhotoImage(resized1)
                    image1.configure(image=logo3)
                    image1.logo = logo3


                    
                    
                    #lmain.after(get_me)
                    

##                else:
##                    showerror("Answer", "Sorry, no plates available")
##
##                  
             


                    
                   
                    if first_time_line is None:
                        first_time_line = line
                        
##                    cap = cv2.VideoCapture('car.mp4')
##
##
##                    ret, frame = cap.read()
##
##                    cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
##
##                    img   = Image.fromarray(cv2image).resize((760, 400))
##                    imgtk = ImageTk.PhotoImage(image = img)
##                    lmain.imgtk = imgtk
##                    lmain.configure(image=imgtk)
                        
                        
button1=Button(master,text="Search",command=get_me,font=(None, 15))
button1.grid(row=5, column=1)

def frame1_capture():
        cap = cv2.VideoCapture("car.mp4")
        
        while not cap.isOpened():
                cap = cv2.VideoCapture("car.mp4")
                cv2.waitKey(1000)
                print ("Wait for the header")

        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        global frameno

        
       
        cap.set(cv2.CAP_PROP_POS_FRAMES,(frameno-30)-1)
        #cap.set(cv2.CAP_PROP_FPS, 5)
                
        
        
        while True:
                
                flag, frame = cap.read()
                
                
                if flag:
                        
                        
                        cv2.imshow("Cam1 video", frame)
                        # The frame is ready and already captured
                        #cv2.imshow('video', frame)
                        #cap.set(cv2.CAP_PROP_FPS, 15)
                        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                        print (str(pos_frame)+" frames")
                else:
                        # The next frame is not ready, so we try to read it again
                        cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
                        print ("Frame is not ready")
                        # It is better to wait for a while for the next frame to be ready
                        cv2.waitKey(1000)

                if cv2.waitKey(80) == 27:
                        break
                if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                        # If the number of captured frames is equal to the total number of frames,
                        # we stop
                        break
                                            
button2=Button(master,text="Play Cam1",command=frame1_capture,font=(None, 15))
button2.grid(row=5, column=3)



def frame2_capture():
        cap = cv2.VideoCapture("car1.mp4")
        
        while not cap.isOpened():
                cap = cv2.VideoCapture("car1.mp4")
                cv2.waitKey(1000)
                print ("Wait for the header")

        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        global frameno

        
       
        cap.set(cv2.CAP_PROP_POS_FRAMES,(frameno-30)-1)
        #cap.set(cv2.CAP_PROP_FPS, 5)
                
        
        
        while True:
                
                flag, frame = cap.read()
                
                
                if flag:
                        
                        
                        cv2.imshow("Cam2 video", frame)
                        # The frame is ready and already captured
                        #cv2.imshow('video', frame)
                        #cap.set(cv2.CAP_PROP_FPS, 15)
                        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                        print (str(pos_frame)+" frames")
                else:
                        # The next frame is not ready, so we try to read it again
                        cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
                        print ("Frame is not ready")
                        # It is better to wait for a while for the next frame to be ready
                        cv2.waitKey(1000)

                if cv2.waitKey(80) == 27:
                        break
                if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                        # If the number of captured frames is equal to the total number of frames,
                        # we stop
                        break
                                            
button2=Button(master,text="Play Cam2",command=frame2_capture,font=(None, 15))
button2.grid(row=5, column=6)



   



                    








##closeButton = Button(master, text = "CLOSE",width = 20, height= 1)
##closeButton.configure(command= lambda: master.destroy())              
##closeButton.place(x=270,y=430)	

  #Display
#master.mainloop()  #Starts GUI





