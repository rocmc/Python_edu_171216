#coding: euc-kr

class Car:                  #클래스 선언
    def drive(self):         #self 호출키워드: 자기자신 호출 (this(담배) 자기자신, super(담배판매처) 상위)
        self.speed = 10

myCar = Car() #Car() 대한 모든 요소 호출 #객체 생성
myCar.clor = "blue" #객체 호출
myCar.model = "E-Class" #객체 호출

myCar.drive() #객체 안의 drive() 메소드가
print(myCar.speed)


