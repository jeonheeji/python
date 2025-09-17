import random
# While 문

i = 1
while i <= 5:
    print("반복문 실행")
    i += 1  # 없을 시에는 무한 루프에 빠짐
print("반복문 종료")

# 실습
# 문제1. 비밀 코드 맞추기
secret_code = "codingon3"
code = input("비밀 코드를 입력하세요 : ",)
while secret_code != code:
    print("틀렸습니다 다시 입력하세요")
    code = input("비밀 코드를 입력하세요 : ",)
print("입장")

# 문제2. 업다운게임

random_value = random.randint(1, 101)
print("1~100사이 무작위 수를 생성 중입니다")
n = int(random_value)
number = int(input("숫자를 입력하세요",))
how_many = 1
while number != n:
    if number > n:
        print(f"{number}보다는 작아요")
        number = int(input("숫자를 입력하세요",))
        how_many += 1
    elif number < n:
        print(f"{number}보다는 커요")
        number = int(input("숫자를 입력하세요",))
        how_many += 1
print(f"{how_many}번 만에 정답을맞췄습니다")
