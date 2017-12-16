#coding: euc-kr

class A:
    def __init__(self):
        print("A 클래스의 생성자 호출!")

class B(A):
    def __init__(self):
        print("B 클래스의 생성자 호출!")
        super().__init__()

class C(A):
    def __init__(self):
        print("C 클래스의 생성자 호출!")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D 클래스의 생성자 호출!")
        super().__init__()

objectD = D()