# for vs while
# for문 : 몇 번 반복할지 정해져 있을 때
# while문 : 조건이 만족하는 동안 계속

# while 조건식:
#    반복할 코드
#    (조건을 변경하는 코드) 중요 i+=1 같은거,,

count = 5

while count > 0:
    print(f"count {count}")
    count -= 1  # 조건 변경하는게 꼭 필요 안그러면 무한루프걸림
print("while문 종료")

# 누적 합계 구하기
total = 0
num = 1

while num <= 100:
    total += num
    num += 1
print(total)

# while문으로 입력 검증하기
# 올바른 입력을 받을 때까지 반복
age = -1  # 초기값

while age < 0 or age > 150:
    age = int(input("나이를 입력하세요:"))

    if age < 0 or age > 150:
        print("올바른 나이를 입력해주세요")
print(f"입력된 나이 : {age}세")

# 비밀번호 확인
correct_password = "python123"
attempt = 0
max_attempts = 3

while attempt < max_attempts:
    password = input("비밀번호를 입력하세요")
    attempt += 1

    if password == correct_password:
        print("성공")
        break
    else:
        remaining = max_attempts-attempt
        if remaining > 0:
            print(f"틀렸음 . {remaining}번 남음")
        else:
            print("실패")
            break

# 무한 루프와 break
while True:
    user_input = input("명령을 입력 (종료 : q)")

    if user_input == 'q':
        print("종료")
        break
    print(f"입력한명령 : {user_input}")

    pass

# 계산기

while True:
    num1 = float(input("첫 번째 숫자"))

    if num1 == 0:
        break

    num2 = float(input("두 번째 숫자"))
    operator = input("연산자 (+,-,*,/)")

    if operator == "+":
        result = num1+num2
    elif operator == "-":
        result = num1-num2
    elif operator == "*":
        result = num1*num2
    elif operator == "/":
        if num2 != 0:
            result = num1/num2
        else:
            print("0으로 나눌 수 없음")
    else:
        print("연산자 다시입력")
        continue
    print(f"결과:{result}")

# while - else 문
i = 10
while i < 15:
    print(i)
    i += 1
else:
    print("정상종료")
