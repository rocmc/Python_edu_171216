#coding: euc-kr


from tkinter import *

def process():
    print("파이선에 오신 것을 환영합니다.")

window = Tk()

l1=Label(window, text="간단한 GUI 프로그램!")
l1.pack()

b1 = Button(window, text="환영합니다", command=process)
b2 = Button(window, text="닫기", command=window.quit)
b1.pack()
b2.pack()

window.mainloop()



