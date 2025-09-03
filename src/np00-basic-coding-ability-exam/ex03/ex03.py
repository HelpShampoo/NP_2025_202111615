
def get_compared_result(num1, num2):
    num3 = num1 + num2
    num4 = num1 << num2
    num5 = num1 * num2

    if num3 > num4 and num3 > num5:
        max_num = num3
    elif num4 > num3 and num4 > num5:
        max_num = num4
    elif num5 > num3 and num5 > num4:
        max_num = num5
    return max_num

print('두 수를 입력하세요:') # 사용자 입력 유도문 출력
num1, num2 = map(int, input().split())   # map에 자료형을 int형으로 지정, split으로 문자열 분리, input으로 사용자 입력 받음 
result = get_compared_result(num1, num2) # 두 수의 덧셈, 비트 시프트, 곱셈 연산을 수행하고 각 연산의 결과값 중 가장 큰 값을 반환하는 함수 호출
print('두 수', num1, num2, '의 덧셈, 비트 시프트, 곱셈 연산 결과중 가장 큰 값은', result, '입니다.')  # 각 연산의 결과값 비교하여 가장 큰 값 출력2