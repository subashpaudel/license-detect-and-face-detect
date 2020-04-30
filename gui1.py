from tkinter import *
import csv

master = Tk()

b1 = StringVar()
#v1 = StringVar()
#v2 = StringVar()
#v3 = StringVar()

a = Label(master, text="plate", font="Verdana 10 bold").grid(row=8, column=1, columnspan=2, pady=15)
b = Label(master, text="Platenumber").grid(row=9, column=1, sticky='w')
c = Label(master, text="ID:").grid(row=10, column=1, sticky='w')
cc = Label(master, text="")
d = Label(master, text="Image path: ").grid(row=11, column=1, sticky='w')
dd = Label(master, text="")
e = Label(master, text="date and time:").grid(row=12, column=1, sticky='w')
ee = Label(master, text="")
f = Label(master, text="accuracy:").grid(row=12, column=1, sticky='w')
ff = Label(master, text="")

def name():
    with open("file.csv") as fh:
        for row in fh:
            if (b1.get()) in row:
                platenumber = row[0:row.find(',')]
                row=row.replace(player_name+',','')
                #print(row)
                firstService=row[0:row.find(",")]
                row=row.replace(firstService+',','')                
                points_firstserve=row[0:row.find(",")]
                row=row.replace(points_firstserve+',','')                
                points_secondserve=row[0:row.find(",")]
                row=row.replace(points_secondserve+',','')    
                cc['text'] += " "+firstService
                #v1.set(firstService)
                cc.grid(row=10, column=2, sticky='w')
                #v2.set(points_firstserve)
                dd['text'] += " "+points_firstserve
                dd.grid(row=11, column=2, sticky='w')
                #v3.set(points_secondserve)
                ee['text'] += " "+points_secondserve
                ee.grid(row=12, column=2, sticky='w')                

myb1 = Entry(master, textvariable=b1)

myb1.insert(10, "Andy Murray")

myb1.grid(row=9, column=2)

button1 = Button(master, text='Run', command=name, bg="light green", font="Verdana 9 bold")
button2 = Button(master, text='Quit', command=quit, bg="red", font="Verdana 9 bold")

button1.grid(row=15, column=2, ipadx=50, pady=10)
button2.grid(row=15, column=3, ipadx=50, pady=10, padx=5)

master.geometry("850x500+300+100")
master.bind('<Return>', name)
master.bind('<Escape>', quit)
mainloop()
