# 실습 2. 가변인자 연습하기
# 문제 1. 숫자 여러 개의 평균 구하기
def average(*args):
    return sum(args)/len(args)


num = input("숫자들을 입력하세요:")
num_list = list(map(float, num.split()))
print(average(*num_list))

# 문제 2. 가장 긴 문자열 찾기


def max_word(*args):
    return max(args, key=len)


word = input("단어를 입력하세요")
word_list = list(word.split())
print(max_word(*word_list))

# 문제 3. 사용자 정보 출력 함수


def print_if(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_if(name="a", age=15, email="b")

# 문제 4. 할인 계산기


def discount(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}의 할인된 가격은 {value*0.9}")


discount(apple="1000", banana="2000", cherry="3000")
