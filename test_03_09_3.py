#coding: euc-kr

from tkinter import *
root = Tk()

lbl = Label(root, text="����")
lbl.grid(row=0, column=1) #row = �� , column = ĭ
# lbl.pack()

txt = Entry(root)
txt.grid(row=1, column=1)
# txt.pack()

btn = Button(root, text="OK", width=15)
btn.grid(row=2, column=1)
# btn.pack() #��ġ ������

root.mainloop()
