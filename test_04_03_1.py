#coding: euc-kr


from tkinter import *

def process():
    print("���̼��� ���� ���� ȯ���մϴ�.")

window = Tk()

l1=Label(window, text="������ GUI ���α׷�!")
l1.pack()

b1 = Button(window, text="ȯ���մϴ�", command=process)
b2 = Button(window, text="�ݱ�", command=window.quit)
b1.pack()
b2.pack()

window.mainloop()



