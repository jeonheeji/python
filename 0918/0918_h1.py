# 중첩 while문

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i}X{j}={i*j}")
    print()

i = 2
while i < 10:
    j = 1
    while j < 10:
        print(f"{i}X{j}={i*j}")
        j += 1
    i += 1
    print()

# 실습 3. 중첩 while문 연습문제
# 문제1번 . 로그인 시스템 구현
correct_id = "abc"
correct_pw = "def"

id = input("id를 입력하세요 :")

while id != correct_id:
    print("id가 존재하지 않습니다")
    id = input("id를 입력하세요")
    if id == correct_id:
        pw = input("pw를 입력하세요")
        while pw != correct_pw:
            print("비밀번호가 틀렸습니다")
            pw = input("pw를 입력하세요")
print("로그인 성공!")
