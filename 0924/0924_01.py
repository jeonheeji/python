# 파일 입출력
# 프로그램이 파일을 읽고 쓰는 작업
# 프로그램이 종료되어도 데이터를 보관할 수 있는 유일한 방법
# 프로그램의 데이터는 메모리에 저장 / 프로그램이 종료되면 메모리의 데이터는 사라짐
# 파일로 저장하면 하드디스크에 영구 보관가능!

# 파일 입출력이 필요한 상황
# 1. 설정파일저장 : 게임설정, 프로그램옵션
# 2. 데이터 백업 : 중요한 정보 보관
# 3. 로그 기록 : 프로그램 실행 기록, 에러 추적
# 4. 데이터 교화 : 엑셀, csv 파일로 다른 프로그램과 데이터 공유
# 5. 대용량 처리 : 메모리에 다 못 담는 빅데이터 처리


# 1. 파일열기
file = open('data.txt', 'r', encoding='utf-8')

# 2. 파일 작업
content = file.read()
print(content)

# 3. 파일 닫기
file.close()

# 가장안전한 방법!
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
# 자동으로 닫기! -> 파일 누수의 위험이 적어짐

# 새 파일 생성 또는 덮어쓰기
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello Wold!\n")
    f.write("파이썬 파일 입출력\n")

with open("output.txt", "w", encoding="utf-8")as f:
    f.write("추가된내용\n")  # 싹날리고 덮어씀

with open("output.txt", "a", encoding="utf-8")as f:
    f.write("진짜추가된내용")  # a로 해야 추가됨!

# 1. read() - 파일전체를 하나의 문자열로
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # 전체내용 읽기
    print(content)

# 1-1. read(크키) - 저장한 크기 만큼만
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read(3)  # 3만큼만 읽기
    print(content)

# 2. readline() - 한줄씩 읽기
with open("data.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1.strip())
    print(line2.strip())  # strip은 공백 제거

# 2-2. readline()-for 문
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
print()

# 2-3. readlines()
with open('data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # ['첫줄\n','둘쨰줄\n',,,]

    for line in lines:
        print(line.strip())
print()
