#! /usr/env/python3

from tkinter import *

window = Tk()

def convert_kg():
    kg = float(e1_value.get())
    gramm = kg * 1000
    pounds = kg * 2.20462
    ounce = kg * 35.274
    t1.insert(END, gramm)
    t2.insert(END, pounds)
    t3.insert(END, ounce)

def refresh():
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)

b1 = Button(window, text='Execute', command=convert_kg)
#b1.pack()
b1.grid(row=0, column=2)

b2 = Button(window, text="Refresh", command=refresh)
b2.grid(row=0, column=3)

label1 = Label(window, text='kg')
label1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1, rowspan=2)

t1 = Text(window, height=2, width=20)
t1.grid(row=2, column=0)

t2 = Text(window, height=2, width=20)
t2.grid(row=2, column=1)

t3 = Text(window, height=2, width=20)
t3.grid(row=2, column=2)

window.mainloop()
