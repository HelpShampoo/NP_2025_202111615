
def get_count_char_of_string(string, char):
    count = 0 # 문자 개수 저장 변수 선언 및 초기화
    for i in range(0, len(string)): # len(문자열 변수) : 문자열의 길이 반환, 0부터 문자열 길이 -1 까지 반복(두번째 인자는 입력한 값 -1이 최댓값 범위가 됨)
        if string[i] == char: # 문자열의 i번째 문자가 주어진 하나의 문자와 같다면
            if count != 0:
                print(',', end='')
            print(i,end='')
            count += 1
    print() # 문자 개수 출력 문장이 다음 행에 출력되도록 하기 위한 개행
    return count # 문자열에서 발견한 주어진 문자와 동일한 문자의 개수를 반환

string, char = input('문자열을 입력하세요: ').split(' ') # 사용자로부터 문자열과 하나의 문자를 입력받아 space 기준으로 분할하고 각각의 변수에 저장
count = get_count_char_of_string(string, char) # 문자열에서 주어진 문자와 동일한 문자의 개수를 계산하는 함수 호출하여 문자열에서 발견한 주어진 문자와 동일한 문자의 개수를 반환받아 변수에 대입
print(string, '에서', char, '의 개수는', count, '개 입니다.') # 문자열에서 주어진 문자와 동일한 문자의 개수를 출력