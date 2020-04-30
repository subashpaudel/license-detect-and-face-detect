from tkinter import *
#import csv
#import time

    
window = Tk()
window.title("TESTING")
window.geometry("300x300")


label = Label(window, text="Enter the url")
urlInput = StringVar()
inputUser = Entry(window, textvariable=urlInput)

def ascan():
    print("working")
##    with open('file.csv', 'r') as csvfile:
##        datareader = csv.reader(csvfile)
##        for line, row in enumerate(datareader):
##            try:
##                first_column = row[0]
##            except IndexError:
##                continue
##            else:
##            # the file oddly saves with a space after TIME
##                if first_column.strip() == urlInput: 
##                    print(row)
##                    if first_time_line is None:
##                        first_time_line = line
    

​
    
button1 = Button(window,text="Scan", command=ascan)
#button2 = Button(window,text="Report", command=report)


label.pack()
inputUser.pack()
button1.pack()
#button2.pack()



window.mainloop()




