# 튜플
# 순서가 있는 불변 시퀀스
# 한 번 생성되면 수정할 수 없음
# 여러개의 값을 하나로 묶음
# 리스트 사용시 -> 실수로 변경 가능

coordinates_lists = [37.345, 126.432]
coordinates_lists[0] = 0  # 변경가능

coordinates_lists = (37.345, 126.432)
# coordinates_lists[0] = 0  # 에러발생 ! 튜플은 못바꿔용


# 1. 소괄호 사용
emp_tuple = ()
numbers = (1, 2, 3, 4, 5,)
mixed = (1, "hello", 3.14, True)

# 2. 소괄호 없이
number2 = 1, 2, 3, 4, 5
print(type(number2))  # 튜플이라고 뜸

# 3. 튜플 () 생성자 사용
from_list = tuple([1, 2, 3, 4])
print(type(from_list))  # 튜플이라고 뜸
from_str = tuple("hello")

# 4. 단일 요소 튜플(, 필수!!)
single = (1,)
# 요소 하나일 때는 마지막에 콤마 꼮ㄲㄲㄲㄲ 써줘야함
error = (10)  # 튜플 x 정수임

# 5. range로 튜플 생성
range_tuple = tuple(range(1, 10))
print(range_tuple)

# tuple 접근과 슬라이싱
fruits = ('사과', '바나나', '수박', '오렌지', '포도')

print(fruits[1])  # 바나나
print(fruits[-1])  # 포도

print(fruits[1:3])  # 바나나 수박
print(fruits[:2])  # 사과 바나나
print(fruits[::-1])  # 포도 오렌지 수박 바나나 사과

# 슬라이싱으로 새 튜플 생성
first_three = fruits[:3]
last_two = fruits[-2:]

combined = first_three+last_two  # 튜플합치기

# 튜플수정원할시 -> 새로 만들어줘야함 아님 list로 변경해서 수정 후 다시 튜플로
tuple_with_list = ([1, 2], [3, 4])
tuple_with_list[0].append(3)  # ([1,2,3],[3,4])
print(tuple_with_list[0].pop())
print(tuple_with_list)

# 언패킹 -> 요소를 배치
coordinates = (3, 5)
x, y = coordinates
print(f"{x},{y}")

# 직접 언패킹
x, y = (10, 20)  # x=10, y=20

# x, y = (10, 20, 30)  # 에러 -> 개수가 맞아야함
numbers = (1, 2, 3, 4, 5)
# first, middle, last = numbers  # 개수가 맞아야해서 에러남
first, *middle, last = numbers
print(first, *middle, last)  # 가능 *붙인곳에 다들어감

# 빈 리스트 생성
first, *rest = (1,)
print(first)  # 1
print(*rest)  # 비어있음

# 튜플 메서드
numbers = (1, 1, 3, 3, 2, 2, 5, 4, 3)
count_2 = numbers.count(2)  # 2
index_4 = numbers.index(4)  # 7 4라는 숫자가 몇번째 인덱스에 있는지
# 없는 값 검색 시 에러

# 안전한 검색위해서 (튜플에서 검색시)
value = 10
if value in numbers:
    print(f"{value}의 인덱스 : {numbers.index(value)}")
else:
    print(f"{value}는 튜플에 없습니다")

# 튜플의 연산
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1+tuple2)  # (1,2,3,4,5,6)

print(tuple1*3)  # (1,2,3,1,2,3,1,2,3)

# 비교연산도 가능 (사전식 비교)

# 길이, 최대, 최소, 합 튜플에서 가능
numbers = (1, 2, 3, 4)
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
