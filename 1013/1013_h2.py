import pandas as pd
import numpy as np
# 실습

data = {
    "도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],
    "미세먼지": [45, 51, np.nan, 38, 49, np.nan],
    "초미세먼지": [20, np.nan, 17, 18, 22, 19],
    "강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]
}
df = pd.DataFrame(data)

print(f"미세먼지 평균 :{df["미세먼지"].mean()} 미세먼지 중앙값 : {df["미세먼지"].median()}")
print(f"초미세먼지 최대값 : {df["초미세먼지"].max()} 초미세먼지 최솟값 : {df["초미세먼지"].min()}")
print(f"컬럼별 결측값 개수 :\n {df.isna().sum()}")

drop_rows = df.dropna()
print(f"남은데이터 초미세먼지의 평균 : {drop_rows["초미세먼지"].mean()}")

df_zero = df.fillna(0)
print(
    f"미세먼지의 합계 : {df_zero["미세먼지"].sum()} \n 초미세먼지의 합계 : {df_zero["초미세먼지"].sum()} ")

fill_mean = df.copy()
fill_mean["미세먼지"] = fill_mean["미세먼지"].fillna(
    fill_mean["미세먼지"].mean())  # 평균값으로 결측값 채우기
print(f"미세먼지표준편차 : {fill_mean["미세먼지"].std()}")
