# 차원 추가와 제거
# newaxis 와 expand_dims
# 차원을 추가하여 브로드 캐스팅이나 연산 가능하게함

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("원본 \n", arr)
print("모양 \n", arr.shape)

# newaxis -> 차원이 늘어남 !
row_vec = arr[np.newaxis, :]
print("행 벡터", row_vec)
print("행 벡터 shape", row_vec.shape)
col_vec = arr[:, np.newaxis]
print("열 벡터", col_vec)
print("열 벡터 shape", col_vec.shape)

# expand_dims
arr_expended0 = np.expand_dims(arr, axis=0)  # 행추가
arr_expended1 = np.expand_dims(arr, axis=1)  # 열추가
print("axis=0", arr_expended0)
print("axis=1", arr_expended1)

# 제거 squeeze
arr = np.array([[[1, 2, 3]]])
print("원본", arr)
print("원본모양", arr.shape)  # (1,1,3)

squeezed = np.squeeze(arr)
print("제거배열", squeezed)
print("제거배열모양", squeezed.shape)  # 1인걸 모두 제거

squeezed0 = np.squeeze(arr, axis=0)  # 맨앞 차원만 제거! axis=1,axis=2 제거 가능
print("0제거", squeezed0)
print("0제거모양", squeezed0.shape)

# 배열 평탄화 Flattening

# flatten : 항상복사본 반환 안전하지만 메모리양 많음
# ravel : 가능하면 뷰 반환 빠르지만 주의 필요

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("2차원 배열")
print(arr)

flattend = arr.flatten()
print(flattend)  # 1차원으로 나열해줌
flattend[0] = 999
print(arr)
print(flattend)  # 원본값 변화 없음

raveled = arr.ravel()
print("결과", raveled)  # 1차원으로 나열
raveled[0] = 999
print(arr)
print(raveled)  # 원본도 같이 바뀜

raveled_copy = arr.ravel().copy()  # 원본값에는 변화 없음
raveled_copy[1] = 999
print(arr)
print(raveled_copy)

# unique
arr = np.array([1, 2, 3, 2, 1, 3, 2, 3, 3, 1, 4])  # 중복
uniq = np.unique(arr)
print(uniq)  # 중복제거!

uniq, idx, inv, cnt = np.unique(arr, return_index=True,
                                return_inverse=True, return_counts=True)
print(uniq)  # 중복제거된값
print(idx)  # 첫등장 인덱스
print(inv)  # 원본에서의 고유값 인덱스
print(cnt)  # 등장횟수
