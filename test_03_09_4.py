#coding: euc-kr

from tkinter import*

window=Tk()

w=Label(window,text="색깔변환1",bg="red",fg="white")
w.place(x=0,y=0)
w=Label(window,text="색변환2",bg="green",fg="black")
w.place(x=20,y=20)

window.mainloop()
