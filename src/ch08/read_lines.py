class Read :
    def __init__(self, filename: str):
        self.__filename = filename

    def read_lines(self):
        rfile = open(self.__filename, "r", encoding="utf-8")
        line : str = rfile.readline() # 한 줄 씩 읽어서 line에 저장, line : str는 타입 어노테이션을 이용하여 타입 힌트 제공
        while line:
            print(line.strip()) # 앞 뒤 공백 문자 제거
            line = rfile.readline() # 한 줄 씩 읽어서 line에 저장
        rfile.close()

s1 = Read("C:\\Users\\user\\OneDrive - 서원대학교\\Study\\컴퓨터공학 학습자료\\3학년 2학기\\네트워크프로그래밍\\Git repository\\src\\ch08\\test.txt")
s1.read_lines() # Read 클래스의 read_lines() 메서드 호출