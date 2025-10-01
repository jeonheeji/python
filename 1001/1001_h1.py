import numpy as np

# 문제1
arr1 = np.array([5, 12, 18, 7, 30, 25])
mask = (arr1 > 10) & (arr1 < 20)
print(arr1[mask])

# 문제2
arr2 = np.array([10, 15, 20, 25, 30, 35])
mask = (arr2 <= 15) | (arr2 >= 30)
print(arr2[mask])

# 문제3
arr3 = np.array([3, 8, 15, 6, 2, 20])
i = (arr3 >= 10)
arr3[i] = 0
print(arr3)

# 문제4
arr4 = np.array([7, 14, 21, 28, 35])
result = np.where(arr4 >= 20, "high", "low")
print(result)

# 문제5
arr5 = np.arange(0, 10)
i = (arr5 % 2 != 0)
arr5[i] *= 10
print(arr5)

# 문제6
arr6 = np.array([
    [10, 25, 30],
    [40, 5, 15],
    [20, 35, 50]
])
i = (arr6 >= 20) & (arr6 <= 40)
print(arr6[i])

# 문제7
arr7 = np.array([1, 2, 3, 4, 5, 6])
i = ~(arr7 % 3 == 0)
print(arr7[i])

# 문제 8
arr8 = np.random.randint(0, 101, size=10)
i = (arr8 < 50)
arr8[i] = 50
print(arr8)

# 문제 9
arr9 = np.array([
    [5, 50, 95],
    [20, 75, 10],
    [60, 30, 85]
], dtype=object)
i1 = (arr9 >= 70)
i2 = (arr9 >= 30) & (arr9 < 70)
i3 = (arr9 < 30)
arr9[i1] = "A"
arr9[i2] = "B"
arr9[i3] = "C"
print(arr9)
