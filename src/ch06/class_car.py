class Car :
    def __init__(self, color, speed): # 초기화 메소드. self는 객체를 나타냄
        self.color = color # 인스턴스 변수 정의;
        self.speed = speed
    
    def speedUp(self, v): # 메소드의 첫 번째 매개변수는 self
        self.speed = self.speed + v
        return self.speed

    def speedDown(self, v):
        self.speed = self.speed - v # 다른 메소드에서 정의된 변수 접근
        return self.speed
    
mycar = Car('Black', 60) # Car class 객체(인스턴스) 생성
print('색상: ', mycar.color, '속도: ', mycar.speed) # 속성 접근
mycar.color = "Red" # 속성 변경도 가능
print('색상: ', mycar.color)
mycar.speedUp(10) # speedUp() method 호출
print('속도: ', mycar.speed)
mycar.speedDown(20) # speedDown() method 호출
print('속도: ', mycar.speed)