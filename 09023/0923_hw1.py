# 실습1 두좌표 사이 거리 구하기
import random
import math
import datetime
x1, y1 = int(input("x좌표를 입력하세요 : ")), int(input("y좌표를 입력하세요 :"))
x2, y2 = int(input("x좌표를 입력하세요 : ")), int(input("y좌표를 입력하세요 :"))


answer = math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2))
print(round(answer, 2))


# 실습2 최소공배수와 최대공약수

print(f"최대의 간식 개수 (최대공약수): {math.gcd(18, 24)} ")
print(f"포장 단위별로 동시에 맞게 떨어지는 최소 간식개수 (최소공배수):{math.lcm(18, 24)}")

# 실습3 로또 번호 뽑기

seq = list(range(1, 46))
num = random.sample(seq, 6)  # 범위내에서 중복없이 6개 뽑기
num.sort()
print(num)

# 실습4 가위바위보 게임만들기
rc = 1
ppr = 2
sc = 3

computer = random.randint(1, 3)
user = int(input("가위(3),바위(1),보(2)"))

print(f"computer:{computer} vs user:{user}")

if computer == 1:
    if user == 1:
        print("무")
    elif user == 2:
        print("승")
    else:
        print("패")
elif computer == 2:
    if user == 1:
        print("패")
    elif user == 2:
        print("무")
    else:
        print("승")
else:
    if user == 1:
        print("승")
    elif user == 2:
        print("패")
    else:
        print("무")

# 실습5 다음 생일까지 남은 날짜 계산하기

day,date=int(input("생일 월을 입력하세요")),