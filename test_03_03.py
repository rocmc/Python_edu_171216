#coding: euc-kr
# 클래스 상속

class ParentOne:
    def func(self):
        print("ParentOne의 함수 호출!")

class ParentTwo:
    def func(self):
        print("ParentTwo의 함수 호출!")

class Child(ParentOne, ParentTwo):
# class Child(ParentTwo, ParentOne):
    def childFunc(self):
        ParentOne.func(self)
        ParentTwo.func(self)

objectChild = Child()
objectChild.childFunc()

objectChild.func()



