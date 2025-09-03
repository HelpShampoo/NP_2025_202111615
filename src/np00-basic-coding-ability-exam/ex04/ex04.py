
def print_all_bases(num):
    print('10진수', num, '은(는) 10진수로', num, '입니다.')      
    print('10진수', num, '은(는) 2진수로', bin(num), '입니다.')     # 10진수 -> 8진수 변환 함수 oct()
    print('10진수', num, '은(는) 8진수로', oct(num), '입니다.')     # 10진수 -> 16진수 변환 함수 hex()
    print('10진수', num, '은(는) 16진수로', hex(num), '입니다.')    # 10진수 -> 16진수 변환 함수 hex()

num = int(input('숫자를 입력하세요: ')) # 사용자로부터 10진수 정수 입력받아 int형으로 변환 후 변수에 저장
print_all_bases(num) # 10진수 정수를 2진수, 8진수, 16진수로 변환하여 출력하는 함수 호출