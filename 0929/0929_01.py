# Numpy 파이썬에서 과학계산을 위한 핵심 라이브러리
# 데이터과학, 머신러닝, 과학연구에서 가장 중요한 도구

# 파이썬은 인터프리터 언더로 실행속도가 느림
# Numpy는 C언어 -> 연산 빠름
# 메모리 효율성이 좋아짐
# 벡터화 연산 가능 (반복문 없이)

import numpy as np

print("Numpy버전 : ", np.__version__)  # 경로확인 메서드
print("Numpy 설치경로 :", np.__file__)

# 배열 생성
# ndarray(N-dimensional array) Numpy의 핵심 자료구조
# 같은 타입의 요소들을 담는 다차원 컨데이너

arr = np.array([1, 2, 3, 4, 5])

print("1.객체타입 :", type(arr))  # numpy.ndarray
print("2.데이터타입 :", arr.dtype)  # int64
print("3.배열모양 :", arr.shape)  # (5,)
print("4.차원수 :", arr.ndim)  # 1
print("5.전체 요소 수 :", arr.size)  # 5

python_list = [1, 2.5, "3.", True]
numpy_array = np.array([1, 2.5, "3.", True])
print(python_list)  # 숫자는 숫자로 문자는 문자로
print(numpy_array)  # 모든게 문자형으로 자동 변환! -> 모두 하나로 합칠 수 있는것으로 변경

# 리스트와 넘파이 연산차이점

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1+list2)  # [1,2,3,4,5,6]

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1+arr2)  # [5 7 9]

int_array = np.array([1, 2, 3, 4, 5])
print("정수배열", int_array)
print("데이터 타입", int_array.dtype)

# 타입 명시적으로 지정 배열
specified_array = np.array([1, 2, 3, 4, 5], dtype=np.float32)
print("배열", specified_array)
print("데이터 타입", specified_array.dtype)

# 문자열 배열
string_array = np.array(["apple", "banana", "cherry"])
print("문자열 배열", string_array)
print("데이터 타입", string_array.dtype)  # <u6 6글자수가 최대!

# 2차원 배열 (3x3)
matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
print("2차원 배열:", matrix)
print("모양:", matrix.shape)  # (3,3)
print("차원; ", matrix.ndim)  # 2
print("크기:", matrix.size)  # 9


# for문으로 배열 생성 가능
rows = []
for i in range(3):
    row = [i*3+j for j in range(4)]
    rows.append(row)

matrix2 = np.array(rows)
print(matrix2)

# 3차원배열 (2x3x4)
# 2개의 3x4 행렬로 구성
tensor = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
])
print(tensor)
print(tensor.shape)
print(tensor.ndim)

# numpy 내장 함수로 배열 생성 (연속)
# 0부터 9까지
arr1 = np.arange(10)
print(arr1)
arr2 = np.arange(1, 11)
print(arr2)
arr3 = np.arange(1, 21, 2)
print(arr3)
arr4 = np.arange(1, 11, 0.5)  # range는 int만 가능
print(arr4)

# 균등 간격 배열 Linspace
# 시작, 끝 사이를 균등하게 나눈 숫자들
arr1 = np.linspace(0, 10, 5)
print(arr1)  # [0 2.5 5 7.5 10] 0부터 10까지(포함)를 5개요소로 균등하게 나눔
arr11 = np.linspace(0, 15, 4)
print(arr11)  # [0,5,10,15]

arr2 = np.linspace(0, 10, 5, endpoint=False)  # 끝값(10)을 제외하고 균등하게 나눔
print(arr2)

arr3 = np.linspace(0, 10, 4, endpoint=False)
print(arr3)  # [0 2.5 5 7.5]

arr4 = np.linspace(0, 15, 5, endpoint=False)
print(arr4)
# 로그 간격 배열 logspace
# logspace(start,end,num)

# zeros : 0으로 채운 배열
zeros_1d = np.zeros(5)
print(zeros_1d)  # [0, 0, 0, 0, 0]
zeros_2d_int = np.zeros((3, 4), dtype=int)  # 정수형으로바꿔줌 원래가 실수형임
print(zeros_2d_int)

matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
zeros_copy = np.zeros_like(matrix)
print(zeros_copy)  # 기존모양과 같은 배열에 0을 채워줌

ones_1d = np.ones(5)
print(ones_1d)

# full 특정 값으로 채운 베열
full_array = np.full((3, 4), 7)  # (3x4)배열을 7로 채우겠다

matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
full_like = np.full_like(matrix, 999)  # 배열 모양을 똑같이 999로 모든값을 채움
print(full_like)

empty_array = np.empty((2, 3))
print(empty_array)  # 주의 쓰레기값!

# 3x3 항등행렬
identity = np.eye(3)
print(identity)

# 4x5 행렬에서 대각선이 1
matrix = np.eye(4, 5)
print(matrix)

# 대각선 위치 조정 (k 매개변수)
# k를 통해서 위치조정이 가능 (정방행렬아닐경우)
matrix = np.eye(4, k=1)
print(matrix)
matrix = np.eye(4, k=-1)
print(matrix)

# 정방항등행렬
identity = np.identity(4)  # 4x4 정방항등행렬형식으로 나옴 = eye(4)
print(identity)

# random 배열
# 0과 1 사이의 균일 분포
random_uniform = np.random.rand(3, 3)
print(random_uniform)

# 특정 범위의 균일 분포
low, high = 10, 20
random_range = low+(high-low)*np.random.rand(3, 3)
print(random_range)

uniform = np.random.uniform(low=0, high=100, size=(2, 3))
print(uniform)
