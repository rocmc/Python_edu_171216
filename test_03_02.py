#coding: euc-kr

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):         #self ȣ��Ű����: �ڱ��ڽ� ȣ�� (this(���) �ڱ��ڽ�, super(����Ǹ�ó) ����)
        self.speed = 60

dadCar = Car(0, "silver", "A6")
momCar = Car(1, "white", "520d")
myCar = Car(2, "blue", "E-Class")

print(dadCar.speed, dadCar.color, dadCar.model)
print(momCar.speed, momCar.color, momCar.model)
print(myCar.speed, myCar.color, myCar.model)

myCar.drive()
print(dadCar.speed)
print(momCar.speed)
print(myCar.speed)

# Ŭ����: ����
# ��ü: ���ϱ�, ���ϱ�, ����
# ����, �޼���: ����, ���� (����+����), (����+����)...


