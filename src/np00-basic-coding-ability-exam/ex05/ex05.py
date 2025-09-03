def print_sum_range(num1, num2):
    result = 0 # 합계 저장 변수 선언 및 초기화
    for num in range(num1, num2 + 1): # range의 두 번째 인자는 범위에 자기자신을 포함하지 않는것 같으므로 num2 + 1을 하면 1부터 3의 범위가 됨
        result += num
    print(num1, '부터', num2, '까지의 합은', result, '입니다.')

num1, num2 = map(int, input('두 수를 입력하세요: ').split()) # 사용자로부터 두 개의 정수를 입력받아 변수에 저장
print_sum_range(num1, num2) # 두 수 사이의 모든 정수의 합을 계산하여 출력하는 함수 호출