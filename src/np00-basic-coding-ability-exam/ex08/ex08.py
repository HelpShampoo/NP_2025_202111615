
def get_sum_of_odd(num1, num2):
    result = 0 # 홀수 합 저장 변수 선언 및 초기화
    for i in range(num1, num2 + 1): # num1부터 num2까지 반복(두번째 인자는 입력한 값 +1이 최댓값 범위가 됨)
        if i % 2 == 1: # i가 홀수라면
            result += i # 홀수 합 변수에 i를 누적하여 더함
    return result # num1부터 num2까지의 범위에서 발견한 모든 홀수의 합을 반환

num1, num2 = map(int, input('두 정수를 입력하세요: ').split(' ')) # 사용자로부터 두 개의 정수를 입력받아 space 기준으로 분할하고 각각의 변수에 정수형으로 변환하여 저장
sum = get_sum_of_odd(num1, num2) # num1부터 num2까지의 범위에서 발견한 모든 홀수의 합을 계산하는 함수 호출하여 반환받아 변수에 대입
print(num1, '부터', num2, '까지의 범위에서 발견한 모든 홀수의 합은', sum, '입니다.') # num1부터 num2까지의 범위에서 발견한 모든 홀수의 합을 출력