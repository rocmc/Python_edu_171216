#coding: euc-kr

class A:
    def __init__(self):
        print("A Ŭ������ ������ ȣ��!")

class B(A):
    def __init__(self):
        print("B Ŭ������ ������ ȣ��!")
        A.__init__(self)

class C(A):
    def __init__(self):
        print("C Ŭ������ ������ ȣ��!")
        A.__init__(self)

class D(B, C):
    def __init__(self):
        print("D Ŭ������ ������ ȣ��!")
        B.__init__(self)
        C.__init__(self)

objectD = D()