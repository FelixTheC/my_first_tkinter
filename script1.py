#! /usr/env/python3

from tkinter import *

window = Tk()

def km_to_miles():
    km = float(e1_value.get())
    miles = km*1.6
    t1.insert(END, miles)

def refresh():
    t1.delete(1.0, END)

b1 = Button(window, text='Execute', command=km_to_miles)
#b1.pack()
b1.grid(row=0, column=0)

b2 = Button(window, text="Refresh", command=refresh)
b2.grid(row=0, column=1)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=1, column=0, rowspan=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=3)

window.mainloop()
