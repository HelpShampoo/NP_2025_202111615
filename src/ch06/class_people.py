class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name
        
    def introMe(self):
        print("Name :", self._name, "age :", str(self.__age))

class Teacher(People):
    def __init__(self, age=0, name=None, school=None):
        super().__init__(age, name) # 부모 클래스의 속성 할당. self 없음
        self.__school = school # 자신의 인스턴스 변수 추가
        
    def showSchool(self):
        print("School :", self.school)
        
p1 = People(20, "Lee")  # People 객체 생성
p1.introMe()    # People.introMe() 메서드 호출

t1 = Teacher(48, "Kim", "HighSchool") # teacher 객체 생성
t1.introMe()   # People.introMe() 메서드 호출 

t1.showSchool()  # Teacher.showSchool() 메서드 호출

# 18행 t1.introMe() 에서 Teacher 클래스에는 introMe()가 정의되어 있지 않으나 부모 클래스인 People의 introMe()를 상속 받았으므로 t1에서 introMe() 호출 가능
# 23행 t1.showSchool() 에서 Teacher 클래스에 추가된 showSchool() 메소드 호출