#coding: euc-kr
# Ŭ���� ���

class ParentOne:
    def func(self):
        print("ParentOne�� �Լ� ȣ��!")

class ParentTwo:
    def func(self):
        print("ParentTwo�� �Լ� ȣ��!")

class Child(ParentOne, ParentTwo):
# class Child(ParentTwo, ParentOne):
    def childFunc(self):
        ParentOne.func(self)
        ParentTwo.func(self)

objectChild = Child()
objectChild.childFunc()

objectChild.func()



