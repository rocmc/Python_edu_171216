#coding: euc-kr

from tkinter import *
root = Tk()

lbl = Label(root, text="성명")
lbl.pack()

txt = Entry(root)
txt.pack()

btn = Button(root, text="OK")
btn.pack() #배치 관리자

root.mainloop()
