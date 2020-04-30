from tkinter import *
import csv

from PIL import ImageTk,Image

##def datareader(self):
##    """Create a csv reader."""
##    with open(self.infile, 'r') as inf:
##        logging.info('Infile name: {0}'.format(inf))
##        file_data = inf.readlines()
##    self.csv_reader = reader(file_data, quotechar='"')

##def get_me():
##    entry_value = entry.get()
##    first_time_line = None
##    FILE='file'
##    with open(str(FILE) + '.csv', 'r') as csv_file:
##        q2 = csv.reader(csv_file, delimiter=',', quotechar='|')
##
####    with open('file.csv', 'r').readlines() as csvfile:
####        datareader = csv.reader(csvfile)
##    for row in q2:
##        try:
##            first_column = row[0]
##        except IndexError:
##            continue
##        else:
##            # the file oddly saves with a space after TIME
##            if first_column.strip() == entry_value: 
##               answer.insert(END,row)
##            if first_time_line is None:
##                first_time_line = line

window = Tk()
window.title("TESTING")
window.geometry("300x300")


label = Label(window, text="Enter the url")
#imagelabel=Label(window,text="image")


##logo=(Image.open("C:\\Users\\subashpaudel\\Desktop\\openalpr_64\\cropedImages\\23.jpg"))
##resized=logo.resize((200,200),Image.ANTIALIAS)
##logo2=ImageTk.PhotoImage(resized)
##
##image1=Label(window,image=logo2)


image1=Label(window)

image1.pack(side='top')
#image1['image']=logo




T = Text(window, height=10, width=30)

urlInput = StringVar()
inputUser = Entry(window, textvariable=urlInput)



def get_me():
    
    first_time_line = None

    with open('file.csv','r') as csvfile:
        datareader = csv.reader(csvfile)
        for line, row in enumerate(datareader):
            try:
                first_column = row[0]
            except IndexError:
                continue
            else:
            # the file oddly saves with a space after TIME
                #print(first_column.strip())
                
                if first_column.strip() == urlInput.get(): 
                    #print(row)
                    
                    string_output='PLATE='+row[0]+'\n'
                    string_output1='Count='+row[1]

##                    logo=(Image.open("C:\\Users\\subashpaudel\\Desktop\\openalpr_64\\cropedImages\\23.jpg"))
##                    resized=logo.resize((200,200),Image.ANTIALIAS)
##                    logo2=ImageTk.PhotoImage(resized)
##
##                    image1=Label(window,image=logo2)
##                    path=row[2]
##
##                    #logo1=(Image.open("C:\\Users\\subashpaudel\\Desktop\\openalpr_64\\cropedImages\\15.jpg"))
##                    logo1=Image.open(path)
##
##                    resized1=logo1.resize((200,200),Image.ANTIALIAS)
##                    logo3=ImageTk.PhotoImage(resized1)
##                    image1.configure(image=logo3)
##                    image1.logo = logo3
             


                    
                    #logo=ImageTk.PhotoImage(Image.open("C:\\Users\\subashpaudel\\Desktop\\openalpr_64\\cropedImages\\23.jpg"))
                    #imagelabel['image']=logo
##                    image1=Label(window)
##                    image1['image']=logo
##                    image1.pack()
                    T.insert(END,string_output)
                    T.insert(END,string_output1)
                    
                    #T.image_create(END,image=logo)
                    if first_time_line is None:
                        first_time_line = line






    


    

button1 = Button(window,text="Scan", command=get_me)
#button2 = Button(window,text="Report", command=report)


label.pack()
T.pack()
inputUser.pack()
button1.pack()

#imagelabel.pack()
#image1.pack()

#button2.pack()



window.mainloop()

