import numpy as np

# 문제1
arr = np.arange(10, 30, 2)
print("문제1: ", arr[1:6:2])

# 문제2
arr = np.arange(1, 10).reshape(3, 3)
print("문제2: ", arr[[0, 1, 2], [0, 1, 2]])

# 문제3
arr = np.arange(1, 13).reshape(3, 4)
arr[:, -1] = -1
print("문제3: \n", arr)

# 문제4
arr = np.arange(1, 17).reshape(4, 4)
print("문제4 - 행역순 : \n", arr[::-1])
print("문제4 - 열역순 : \n", arr[:, ::-1])

# 문제 5
arr = np.arange(1, 21).reshape(4, 5)
arr_copy = arr[1:3, 1:4].copy()
print("문제5 - 부분배열 : \n", arr_copy)
