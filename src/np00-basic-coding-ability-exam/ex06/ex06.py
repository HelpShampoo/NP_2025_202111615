def print_sum_digits(number):
    digits = [] # 각 자리 숫자를 저장할 리스트 정의
    while number > 0:
        digits.append(number % 10) # 1의 자리 숫자 분리
        number //= 10 # number를 10으로 나누어 다음 자릿수로 이동
    digits.reverse() # 리스트의 순서를 뒤집어 각 자리 숫자가 원래 순서대로 되도록 함
    result = sum(digits) # 리스트에 저장된 각 자리 숫자의 합을 계산 (sum 함수는 순환접근 가능한 자료형의 모든 요소의 합을 계산하는 파이썬 내장함수)
    print(number, '의 각 자리의 십진수의 합은', result, '입니다.')

num = int(input('정수를 입력하세요: ')) # 사용자로부터 정수 입력받아 int형으로 변환 후 변수에 저장
print_sum_digits(num) # 정수의 각 자리 숫자의 합을 계산하여 출력하는 함수 호출