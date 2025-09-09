
def get_year_of_admission(student_id):
    """
    학생 ID에서 입학 연도를 추출하는 함수
    학생 ID의 첫 두 자리는 입학 연도를 나타냅니다.
    예를 들어, '23'은 2023년을 의미합니다.
    """
    year_of_admission = student_id[:4]  # 문자열 슬라이싱으로 문자열의 처음부터 4번째 글자 전까지 잘라낸다
    return year_of_admission    # 추출한 입학 연도 반환

studentid = input("학생 ID를 입력하세요 (예: 20230001): ")
year_admission = get_year_of_admission(studentid)
print(f"입학 연도는 {year_admission}년입니다.")