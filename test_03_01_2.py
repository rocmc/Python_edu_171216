#coding: euc-kr

class Car:                  #클래스 선언

    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):         #self 호출키워드: 자기자신 호출 (this(담배) 자기자신, super(담배판매처) 상위)
        self.speed = 60

myCar = Car(0, "blue", "E-Class")

print(myCar.speed)
print(myCar.color)
print(myCar.model)
print("자동차를 주행합니다.")

myCar.drive() #객체 안의 drive() 메소드가 호출
print(myCar.speed)

