
def get_contact_info():
    # 연락처들을 담을 리스트 초기화
    contacts = []

    while True:
        name = input("이름을 입력하세요 (종료하려면 0 입력): ")
        if name == '0':
            break

        age = input("나이를 입력하세요 (종료하려면 0 입력): ")
        if age == '0':
            break

        # 나이는 숫자로 변환 (잘못된 입력에 대비)
        try:
            age = int(age)
        except ValueError:
            print("잘못된 나이 형식입니다. 다시 입력해주세요.")
            continue # 다음 반복으로 넘어감

        phone_number = input("전화번호를 입력하세요: ")

        # 한 사람의 정보를 딕셔너리로 묶기
        contact = {
            'name': name,
            'age': age,
            'phone_number': phone_number
        }
        # 딕셔너리를 리스트에 추가
        contacts.append(contact)
        print("--- 연락처가 추가되었습니다. ---")

    print("\n입력이 완료되었습니다.")
    return contacts     # 지금까지 입력받은 연락처들을 저장한 딕셔너리의 모음인 리스트 반환

def print_contacts(contacts):
    """
    연락처 목록을 전달받아 콘솔에 순서대로 출력합니다.
    """
    print("\n--- 전체 연락처 목록 ---")
    # 리스트에 연락처가 하나도 없는 경우를 확인
    if not contacts:
        print("저장된 연락처가 없습니다.")
        return

    # for문을 이용해 리스트의 각 요소를 순회하며 출력
    for i, contact in enumerate(contacts, 1):   # enumrate는 순차적인 자료구조로 되어있는 변수들을 순회할 때 사용하는 내장함수
        print(f"{i}. 이름: {contact['name']}, 나이: {contact['age']}, 전화번호: {contact['phone_number']}")    # 각 연락처의 정보들을 출력

contacts = get_contact_info() # 연락처를 딕셔너리로 묶은 리스트를 반환받아 저장
print_contacts(contacts) # 연락처 리스트를 전달하여 출력