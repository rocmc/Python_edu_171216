#coding: euc-kr

class Car:                  #Ŭ���� ����

    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):         #self ȣ��Ű����: �ڱ��ڽ� ȣ�� (this(���) �ڱ��ڽ�, super(����Ǹ�ó) ����)
        self.speed = 60

myCar = Car(0, "blue", "E-Class")

print(myCar.speed)
print(myCar.color)
print(myCar.model)
print("�ڵ����� �����մϴ�.")

myCar.drive() #��ü ���� drive() �޼ҵ尡 ȣ��
print(myCar.speed)

