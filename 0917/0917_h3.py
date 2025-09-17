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
times = 0
sum_age = 0
num = 0
while times < 5:
    num = int(input("나이를 입력하세요:"))
    if num <= 0 or num > 120:
        continue

    else:
        times += 1
        sum_age += num

print(f"총 나이 합계는 {sum_age}, 평균은 {sum_age / 5}입니다")
