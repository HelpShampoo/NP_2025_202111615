class Calc:
    count = 0 # 클래스 변수
    def add(self, a=0, b=0):
        self.a = a # 인스턴스 변수
        self.b = b
        self.count += 1 # 클래스 변수를 self와 함께 사용하면 인스턴스 변수처럼 사용하
        return self.a + self.b
    def minus(self, a,b):
        if a == 0 or b == 0:
            return a - b, self.count
        else:
            return a - b
        
obj = Calc()
print(obj.minus(3,0)) #count 속성 출력
print(obj.minus(3,1))
print(obj.add(1,2)) #count 속성 증가
print(obj.count, Calc.count) # 인스턴스 변수(obj.count)는 변하지만 클래스 변수 Calc.count는 변하지 않음