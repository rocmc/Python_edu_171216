#coding: euc-kr

from tkinter import *


def process():
    e2.insert(0, "123")

window  = Tk()


l1 = Label(window , text="ȭ��")
l2 = Label(window, text="����")


l1.grid(row=0, column=0)
l2.grid(row=1, column=0)


e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="ȭ���漷��", command=process)
b2 = Button(window, text="������ȭ��")
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)

window.mainloop()


