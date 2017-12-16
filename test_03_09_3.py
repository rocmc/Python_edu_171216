#coding: euc-kr

from tkinter import *
root = Tk()

lbl = Label(root, text="성명")
lbl.grid(row=0, column=1) #row = 줄 , column = 칸
# lbl.pack()

txt = Entry(root)
txt.grid(row=1, column=1)
# txt.pack()

btn = Button(root, text="OK", width=15)
btn.grid(row=2, column=1)
# btn.pack() #배치 관리자

root.mainloop()
