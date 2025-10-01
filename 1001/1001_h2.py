import numpy as np

# 실습1
# 문제1
arr = np.array([[10, 20], [30, 40], [50, 60]])
ravel_arr = arr.ravel()
flatten_arr = arr.flatten()
arr[0, 0] = 999
print(ravel_arr)  # 999로 바뀜
print(flatten_arr)  # 안바뀜
# 문제2
img = np.random.rand(32, 32)
new_img = np.expand_dims(img, axis=0)
print(new_img.shape)
# 문제3
img = np.random.randint(0, 255, (1, 28, 28, 1))
new_img = np.squeeze(img, axis=0)  # 맨앞 차원 삭제
new_img = np.squeeze(img, axis=0)  # 그다음 맨앞 차원 삭제
new_img = np.squeeze(img)  # 1인 차원 모두 삭제
print(new_img.shape)
# 문제4
arr = np.array([
    [3, 1, 2, 2],
    [1, 2, 3, 1],
    [2, 2, 1, 4]
])
new_arr = arr.flatten()  # 1차원 배열로 만든후
uniq_arr = np.unique(new_arr)  # 중복제거
uniq_arr.reshape(1, -1)
print(uniq_arr)
