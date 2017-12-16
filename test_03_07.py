#coding: euc-kr

class Human:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2

    def eat(self):
        print("먹고있다..")

    def sleep(self):
        print("자고있다..")

    def hear(self):
        print("듣고있다..")


class Man(Human):
    def walk(self):
        print("걷고있다..")

kkw = Man()

kkw.hear()
kkw.walk()
print(kkw.nose)
print()

www = Human() #class Human 항목 해당
www.eat()
www.walk() #class Human 항목에는 walk 내용이 없음

