num_1 = 5       # 정수 5를 저장하는 변수
num_2 = 2.14    # 실수 2.14를 저장하는 변수
greeting = 'Hello'   # 문자열형 'Hello'를 저장하는 변수
number_list = [ 1, 2, 3, 4 ] # 숫자의 목록 1, 2, 3, 4를 저장하는 리스트
str_list = [ 'Apple', 'Banana', 'Cherry', 'Durian' ] # 문자열형 목록 'Apple', 'Banana', 'Cherry', 'Durian'를 저장하는 리스트
PI = 3.141592   # 원주율 3.141592를 저장하는 변수(변수 이름을 모두 대문자로 작성하여 상수처럼 다루도록 변수의 이름을 명명함)

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    phone_number: str

human = Person(name="", age=0, phone_number="")
human.name = input("이름을 입력하세요: ")
human.age = int(input("나이를 입력하세요: "))
human.phone_number = input("전화번호를 입력하세요: ")

print(num_1)
print(num_2)
print(greeting)
print(number_list)
print(str_list)
print(PI)
print(human)