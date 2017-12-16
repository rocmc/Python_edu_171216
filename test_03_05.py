#coding: euc-kr

class A:
    def __init__(self):
        print("A Ŭ������ ������ ȣ��!")

class B(A):
    def __init__(self):
        print("B Ŭ������ ������ ȣ��!")
        super().__init__()

class C(A):
    def __init__(self):
        print("C Ŭ������ ������ ȣ��!")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D Ŭ������ ������ ȣ��!")
        super().__init__()

objectD = D()