# 람다 함수
# 람다 함수는 이름 없는 한 줄짜리 간단한 함수

def square(x):
    return x**2


def square_lambda(x): return x**2


print(square(5))
print((lambda x: x**2)(5))

# 여러 매개변수


def add(x, y): return x+y


print(add(3, 4))

# map(): 모든 요소에 함수 적용
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# filter 조건에 만족하는 수만 나옴
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# sorted() 정렬 기준 지정
students = [
    {"name": "홍", 'score': 80},
    {"name": "김", 'score': 70},
    {"name": "박", 'score': 85}
]
students.sort(key=lambda x: x['score'], reverse=True)
for student in students:
    print(f"{student["name"]}:{student['score']}")
