#coding: euc-kr

import math

class Shape(object):
    def __init__(self, name):
        self.name = name

    def calcArea(self):
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
    shapes = [Circle('원', 2)
        , Quadrangle('사각형', 2, 2)
        , Triangle('삼각형', 2, 2)]
    for s in shapes:
        print('{} : {}'.format(s.name, s.calcArea()))


main()
