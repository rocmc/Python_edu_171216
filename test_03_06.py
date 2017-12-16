#coding: euc-kr

import math


class Shape(object):
    # ����

    # ������ ���̸� ���ϴ� ���� API�� ���´�.

    def __init__(self, name):
        self.name = name

    def calcArea(self):
        '���̸� ���ϴ� API. ��� Ŭ�������� ���� �����ؾ� ��'
        raise NotImplemented


class Circle(Shape):
    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def calcArea(self):
        return self.r * self.r * math.pi


class Quadrangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calcArea(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calcArea(self):
        return self.width * self.height / 2


def main():
    # ��, �簢��, �ﰢ������ ����Ʈ�� �����.
    shapes = [Circle('��', 2)
        , Quadrangle('�簢��', 2, 2)
        , Triangle('�ﰢ��', 2, 2)]

    # �� ������ ���̸� ���Ѵ�.
    for s in shapes:
        print('{} : {}'.format(s.name, s.calcArea()))


main()
