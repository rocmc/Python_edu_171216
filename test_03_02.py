#coding: euc-kr

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):         #self 호출키워드: 자기자신 호출 (this(담배) 자기자신, super(담배판매처) 상위)
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

# 클래스: 계산기
# 객체: 더하기, 곱하기, 빼기
# 변수, 메서드: 숫자, 변수 (숫자+숫자), (변수+변수)...


