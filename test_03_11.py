#coding: euc-kr
from tkinter import *

window  = Tk()

l1 = Label(window, text="ȭ��")
l2 = Label(window, text="����")
l1.pack()
l2.pack()

e1 = Entry(window)
e2 = Entry(window)
e1.pack()
e2.pack()

b1 = Button(window, text="ȭ��->����")
b2 = Button(window, text="����->ȭ��")
b1.pack()
b2.pack()

window.mainloop( )