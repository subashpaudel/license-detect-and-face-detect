from tkinter import *
import csv
 
window = Tk()
 
window.title("search for license data")
 
window.geometry('350x200')
 
lbl = Label(window)
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=20)
 
txt.grid(column=1, row=0)
 
def clicked():
    first_time_line = None

with open('file.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for line, row in enumerate(datareader):
        try:
            first_column = row[0]
        except IndexError:
            continue
        else:
            # the file oddly saves with a space after TIME
            if first_column.strip() == txt: 
               Label=label( print(row))
            if first_time_line is None:
                first_time_line = line


    


 
btn = Button(window, text="Search",command=clicked)
 
btn.grid(column=2, row=0)
 
window.mainloop()
