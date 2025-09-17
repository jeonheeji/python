# 연습문제(2)
# 문제1 비밀 코드 맞추기(2)
secret_code = "codingon3"
code = input("비밀 코드를 입력하세요")

while code != secret_code:
    print("다시 시도하세요")
    code = input("비밀 코드를 입력하세요")
    if code == secret_code:

        break
print("정답")

# 문제2 유효한 나이만 평균내기
num1, num2, num3, num4, num5 = input("숫자를 입력하세요", sep=",")
i = 1
# while i > 5:
# if int(input("숫자를 입력하세요")) <= 0 or int(input("숫자를 입력하세요"))
