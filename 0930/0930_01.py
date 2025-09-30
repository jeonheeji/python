# 배열 인덱싱과 슬라이싱

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(arr)

# 양수 인덱스 (0부터 시작)
print("첫번쩨요쇼", arr[0])  # 10

# 음수 인덱스 (뒤에서부터)
print("마지막요쇼", arr[-1])  # 70

arr[0] = 100  # 10 -> 100

# 배열 슬라이싱
print("2부터 5까지", arr[2:5])  # 30,40,50
print("짝수인덱스만", arr[::2])  # 10,30,50,70

# 슬라이싱으로 값 수정 -> 리스트에서는 슬라이싱으로 값바꿀 수 없음
arr[2:5] = 100  # 2,3,4 인덱스 모두가 100으로 바뀜
print(arr)

# 독립적인 복사본이 필요한 경수
original = np.array([1, 2, 3, 4, 5])
copy = original[1:4].copy()  # original은 변경안돼 view는 변경됌


# 2차원 배열
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix)

# 요소 접근
print(matrix[0, 0])  # 1

# 배열 모양 변경, 조작 -> size에 맞게 넣을 수 있음 -1은 자동으로 개수에 맞춰서 넣게 도와줌
arr_1d = np.array([1, 2, 3, 4, 5, 6])
print("shape", arr_1d.shape)  # 이게 왜 (6,)? (1,6)이자네..;;
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("shape", arr_2d.shape)

# 스칼라연산 굿 모든 연산 다 가능
a = np.array([1, 2, 3, 4, 5])
scalar = 10
print(a+scalar)

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

print(A+B)
print(A*B)  # 각 원소들끼리 그냥 곱하기

A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [7, 8],
    [9, 10]
])
print(A@B)  # 원래 행렬의 곱셈

# 브로드캐스팅
# 서로 다른 모양의 배열간 연산을 가능하게하는 기능
arr = np.array([1, 2, 3, 4, 5])
scalar = 10
# 스칼라가 자동으로 배열 크기로 브로드캐스드 됨
# -> [10,10,10,10,10]

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
vector = np.array([10, 20, 30])
print(matrix+vector)
