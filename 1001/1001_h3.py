import numpy as np
# 실습2
# 문제1
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
a_b = np.concatenate([a, b], axis=0)
print(a_b)

# 문제2
a = np.arange(12)
a2 = np.split(a, 3)
print(a2)

# 문제3
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
arr3 = np.stack((a, b, c), axis=0)
print(arr3)

# 문제4
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
a_b = np.stack([a, b], axis=0)
print(a_b.shape)

# 문제5
arr = np.arange(8)
arr5 = np.split(arr, [2, 5])
print(arr5)

# 문제6
a = np.ones((2, 3))
b = np.zeros((2, 3))
a2 = np.stack(a, axis=0)
b2 = np.stack(b, axis=1)
print(a2.shape)
print(b2.shape)
