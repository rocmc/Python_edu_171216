#coding: euc-kr


from tkinter import *

def process():
    print("�ȳ��ϼ���?")

window = Tk()
button = Button(window, text="Ŭ���ϼ���", command=process)

button.pack()
window.mainloop()

