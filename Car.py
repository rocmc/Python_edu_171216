#coding: euc-kr

class Car:                  #Ŭ���� ���� #���ϸ� ���� �� Ŭ���� ������ �����ؾ� ���డ���ϴ�.
    def drive(self):         #self ȣ��Ű����: �ڱ��ڽ� ȣ�� (this(���) �ڱ��ڽ�, super(����Ǹ�ó) ��������)
        self.speed = 10

myCar = Car() #Car() ���� ��� ��� ȣ�� #��ü ����
myCar.color = "blue" #��ü ȣ��
myCar.model = "E-Class" #��ü ȣ��

myCar.drive() #��ü ���� drive() �޼ҵ尡 ȣ��
print(myCar.speed)
print(myCar.color)
print(myCar.model)

