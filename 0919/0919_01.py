def outer():
    a = 10

    def inner():
        nonlocal a
        a += 5
        print(f"[inner] a : {a}")
    inner()
    print(f"[outer] a : {a}")


outer()

# 함수의 범위
# 변수의 범위란?
# 변수가 접근 가능한 영역을 범위 또는 scope라고 함
# 집= 전역범위 / 방 = 지역범위
# 방안에 물건은 방에서만 사용가능 / 거실의 물건은 집 전체에서 사용가능

# 전역변수 (Global Variale)
global_var = "전역 변수"


def my_fun():
    # 지역변수 (Local Variable)
    local_var = "지역 변수"

    print(global_var)  # 전역변수 접근가능
    print(local_var)  # 지역변수 접근가능


my_fun()
print(global_var)  # 전역변수 접근가능
# print(local_var) 지역변수 접근불가능


# global 키워드 알아보기
# 함수안에서 전역변수를 수정하기위해!

count = 0  # 전역변수

# def increment_wrong():
# count=count+1 # 에러 발생 지역변수 취급이됨


def increment_right():
    global count  # 글로벌 키워드를 통해 전역변수를 수정할 수 있게 됨
    count = count+1


print("초기값", count)  # 0
increment_right()
increment_right()
print("최종값", count)  # 2

score = 0


def add_score(points):
    global score
    score += points
    print(f"점수 획득 현재 점수 : {score}")


def reset_score():
    global score
    score = 0
    print("점수 초기화")


add_score(100)  # 100
add_score(200)  # 300

print(score)  # 300

reset_score  # 점수초기화

print(score)  # 0

# 전역변수 사용주의
# 전역변수는 편리하지만 과도하게 사용하면 코드 복잡해짐

# 나쁜예

total = 0
count = 0


def add_number(num):
    global total, count
    total += num
    count += 1


def get_average():
    global total, count
    return total / count if count > 0 else 0

# 좋은예


def calculate_average(numbers):
    if not numbers:  # 빈 리스트 확인
        return 0
    return sum(numbers)/len(numbers)


numbers = [53, 56, 34, 64]
avg = calculate_average(numbers=numbers)


def num_append(numbers):
    numbers.append(6)


numbers = [1, 2, 3, 4, 5]
print("함수 호출 전: ", numbers)
num_append(numbers)
print("함수 호출 후: ", numbers)

# 어쨌든 리스트는 글로벌 지정없이 가능!!!!!
# 그러나 리스트의 한 인덱스를 글로벌 지정없이 수정하는건 불가능!!!!!!

# 불변타입 : 정수, 실수, 튜플, 문자열
# 함수에 복사본이 넘어감 (함수내 전역변수 수정 불가- global 쓰면 가능)


# 가변타입 : 리스트, 딕셔너리, set
# 함수에 원본 그대로 넘어감 (함수내 전역변수 수정 가능)

new_dic = {'name': '김철수', 'age': 20}


def change_info(info):

    info['name'] = '이영희'
    info['age'] = 25


print("함수 호출 전 :", new_dic)
change_info(new_dic)
print("함수 호출 후", new_dic)
