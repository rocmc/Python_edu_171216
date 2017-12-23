#coding: euc-kr

from tkinter import *


class Wiget:
     def __init__(self):
          w = Tk()

          w.title('위젯')

          f = Frame(w)

          f.pack()

          self.v1 = IntVar()

          cb = Checkbutton(f, text='진하게', variable=self.v1, command=self.cb)

          cb.grid(row=1, column=1)

          self.v2 = IntVar()

          rb1 = Radiobutton(f, text='남', variable=self.v2, value=1, command=self.rb)

          rb2 = Radiobutton(f, text='여', variable=self.v2, value=2, command=self.rb)

          rb1.grid(row=2, column=1)

          rb2.grid(row=2, column=2)

          f2 = Frame(w)

          f2.pack()

          label = Label(f2, text='이름:')

          label.grid(row=1, column=1)

          self.name = StringVar()

          entry = Entry(f2, textvariable=self.name)

          entry.grid(row=1, column=2)

          button = Button(f2, text='확인', command=self.ok)

          button.grid(row=1, column=3)

          message = Message(f2, text='메세지')

          message.grid(row=1, column=4)

          t = Text(w)

          t.pack()

          t.insert(END, '1234\n')

          t.insert(END, '5678\n')

          t.insert(END, '910')

          w.mainloop()

     def cb(self):
          print(self.v1.get())

     def rb(self):
          print(self.v2.get())

     def ok(self):
          print(self.name.get())

          self.name.set('')


Wiget()
