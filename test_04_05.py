#coding: euc-kr

from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

def update_add():
    update("add")

def update_subtract():
    update("subtract")

def update_reset():
    update("reset")

window = Tk()

l1=Label(window, text="�����հ�:")
l1.pack()

e1=Entry(window)
# e1.grid(row=0, column=1)

b1 = Button(window, text="���ϱ�", command=update_add)
b2 = Button(window, text="����", command=update_subtract)
b3 = Button(window, text="�ʱ�ȭ", command=update_reset)

b1.pack()
b2.pack()
b3.pack()



window.mainloop()
