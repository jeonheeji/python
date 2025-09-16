# 실습2 for문과 range
# 문제 1 입력받은 수의 합 구하기
num = input("숫자를 입력하세요",)
for number in range(1, int(num)+1):
    number += number
print(number)

# 문제2 구구단만들기
num2 = input("정수를 입력하세요 : ",)
for i in range(1, 10):
    print(f"{num2}X{i}={int(num2)*i}")

# 문제3 3의 배수의 합 구하기
sum = 0
for i in range(3, 100, 3):
    sum += i
print(f"3의 배수의 합은?{sum}")

# 문제4 짝수이면서 5의 배수인 수 출력하기
num3 = input("숫자를 입력하세요",)
for i in range(5, int(num3)+1, 5):
    if i % 2 == 0:
        print(i)
