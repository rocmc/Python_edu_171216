#coding: euc-kr

from tkinter import *



class Wiget:

     def __init__(self):

          w=Tk()

          w.title('����')

          f=Frame(w)

          f.pack()

          self.v1=IntVar()

          cb=Checkbutton(f,text='���ϰ�', variable=self.v1,command=self.cb)

          cb.grid(row=1,column=1)

          self.v2=IntVar()

          rb1=Radiobutton(f,text='��', variable=self.v2,value=1,command=self.rb)

          rb2=Radiobutton(f,text='��', variable=self.v2,value=2,command=self.rb)

          rb1.grid(row=2,column=1)

          rb2.grid(row=2,column=2)

          w.mainloop()

     def cb(self):

          print(self.v1.get())

     def rb(self):

          print(self.v2.get())

Wiget()

