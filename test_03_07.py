#coding: euc-kr

class Human:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2

    def eat(self):
        print("�԰��ִ�..")

    def sleep(self):
        print("�ڰ��ִ�..")

    def hear(self):
        print("����ִ�..")


class Man(Human):
    def walk(self):
        print("�Ȱ��ִ�..")

kkw = Man()

kkw.hear()
kkw.walk()
print(kkw.nose)
print()

www = Human() #class Human �׸� �ش�
www.eat()
www.walk() #class Human �׸񿡴� walk ������ ����

