# 배열 결합
# 배열 이어 붙이기
# 같은 차원의 배열들을 특정 축을 따라 연결
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

# 1차원 배열
concat_1d = np.concatenate([a, b, c])
print(concat_1d)  # [1 2 3 4 5 6 7 8 9]

# 2차원 배열
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
concat_v = np.concatenate([A, B], axis=0)
print(concat_v)  # [1 2]
# [3 4]
# [5 6]
# [7 8]
concat_h = np.concatenate([A, B], axis=1)
print(concat_h)  # [1 2 5 6]
# [3 4 7 8]

# vstack, hstack
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vstacked = np.vstack([a, b])
print(vstacked)  # 수직방향 [1,2,3]
# [4,5,6]
hstacked = np.hstack([a, b])
print(hstacked)  # 수평방향 [1 2 3 4 5 6]

# 배열 분할
# split
# 하나의 배열을 여러개의 작은 배열로 나눔
# 데이터를 배치로 나누거나 훈련/검증 세트로 분리할 떄 사용

arr = np.arange(12)
print(arr)  # [0,1,2,3,4,5,6,7,8,9,10,11]
split_equal = np.split(arr, 3)
for i, sub in enumerate(split_equal):
    print(i+1, sub)
    # 1 [0 1 2 3]
    # 2 [4 5 6 7]
    # 3 [8 9 10 11]
split_idx = np.split(arr, [3, 7])  # 인덱스 3하고 7에서 분할 하겠다
print(split_idx)  # [0 1 2] [3 4 5 6] [7 8 9 10 11]

arr = np.arange(24).reshape(4, 6)
print(arr)

row_splits = np.split(arr, 2, axis=0)  # 균등하게 나눌수 있는 숫자만 넣을 수 있음
print(row_splits)  # 행을기준으로 반갈죽
col_splits = np.split(arr, 2, axis=1)
print(col_splits)  # 열을 기준으로 반갈죽

arr = np.array([3, 1, 2, 3, 5, 2])
sorted_copy = np.sort(arr)
print(sorted_copy)  # [1 2 2 3 3 5] # 복사해서 정렬
print(np.sort(arr))  # 원본도 같이 정렬

arr2 = np.array([
    [2, 1, 5],
    [3, 2, 1]
])
sorted_axis0 = np.sort(arr2, axis=0)
print(sorted_axis0)  # [2 1 1 ] \n[3 2 5]
sorted_axis1 = np.sort(arr2, axis=1)
print(sorted_axis1)  # [1 2 5] \n[1 2 3]
sorted_none = np.sort(arr2, axis=None)
print(sorted_none)  # [1 1 2 2 3 5] -> 평탄화 후 정렬

# argsort
names = np.array(["k", "l", "p"])
scores = np.array([85, 92, 70])
for name, score in zip(names, scores):
    print(f"{name} {score}")
# 점수 순으로 정렬
sorted_idx = np.argsort(scores)[::-1]  # 높은순으로 정렬
for i, idx in enumerate(sorted_idx, 1):
    print(f"{i}위 {names[idx]} {scores[idx]}")
