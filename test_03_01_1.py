#coding: euc-kr

class Car:                  #Ŭ���� ����
    def drive(self):         #self ȣ��Ű����: �ڱ��ڽ� ȣ�� (this(���) �ڱ��ڽ�, super(����Ǹ�ó) ����)
        self.speed = 60

myCar = Car() #Car() ���� ��� ��� ȣ�� #��ü ����
myCar.speed = 0
myCar.color = "blue" #��ü ȣ��
myCar.model = "E-Class" #��ü ȣ��
myCar.year ="2017"

print(myCar.speed)
print(myCar.color)
print(myCar.model)
print("�ڵ����� �����մϴ�.")
myCar.drive() #��ü ���� drive() �޼ҵ尡 ȣ��


print(myCar.speed)

