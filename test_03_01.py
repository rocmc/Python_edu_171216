#coding: euc-kr

class Car:                  #Ŭ���� ����
    def drive(self):         #self ȣ��Ű����: �ڱ��ڽ� ȣ�� (this(���) �ڱ��ڽ�, super(����Ǹ�ó) ����)
        self.speed = 10

myCar = Car() #Car() ���� ��� ��� ȣ�� #��ü ����
myCar.clor = "blue" #��ü ȣ��
myCar.model = "E-Class" #��ü ȣ��

myCar.drive() #��ü ���� drive() �޼ҵ尡
print(myCar.speed)


