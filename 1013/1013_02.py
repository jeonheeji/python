import pandas as pd
import numpy as np

data = {
    "이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원"],
    "나이": [23, 35, 31, 40, 28, 34],
    "직업": ["학생", "군인", "장군", "장군", "상인", "왕자"]
}
df = pd.DataFrame(data)

# 인덱싱
print(df["이름"])
print(df[["이름", "직업"]])

# 슬라이싱
print(df[1:3])  # 1행에서 3열 전까지 모든 열 나옴
print(df[-2:])
print(df[-2:]["이름"])  # 원하는 범위에서의 이름만 나옴

# Dataframe의 슬라이싱은 행(Row)기준으로 동작!
# 열 단위 슬라이싱은 명시적으로 지정해야함

# iloc 숫자로
print(df.iloc[0])  # 0번 행 전체
print(df.iloc[:, 1])  # 1번 열 전체
print(df.iloc[2:4, 1])  # 2,3행의 1번째 열

# loc 인덱스명으로
print(df.loc[0])  # 0번 행 전체
print(df.loc[:, "나이"])
print(df.loc[:, ["이름", "나이"]])
print(df.loc[1:3, ["이름", "나이"]])  # loc는 1부터 3까지 마지막 수를 포함함!

# 데이터 정제

# 결측값(missing value)
# 비어있는, 알 수 없는, 기록되지 않은 데이터
# 종류
# None = Python의 빈 객체
# np.nan: Numpy의 Not a Number
# pd.NA : Pandas의 결측값(최신)
# 빈 문자열: "" 또는 ''(공백)
# 특수 값: -99999,99999

missing_types = pd.DataFrame({
    "none_type": [1, 2, None, 4],
    "nan_type": [1, 2, np.nan, 4],
    "empty_string": ["a", "b", "", "d"],
    "whitespace": ["a", "b", " ", "d"],
    "special_value": [1, 2, -999, 4]
})

print(missing_types.isna())  # 결측값인것이 true
print(missing_types.isnull())
print(missing_types.notna())  # 결측값이 아닌 것이 true
print(missing_types.notnull())

# 결측값 통계확인
print("열별 결측값 개수")
print(missing_types.isna().sum())
print("전체 결측값 개수")
print(missing_types.isna().sum().sum())

# 결측값 처리 전략
# 1. 삭제 - 결측값이 있는 행/열제거
# 2. 대체 - 다른 값으로 채우기
# 3. 예측 - 앞뒤 값이나 패턴으로 추정

sales_data = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=7),
    "sales": [100, 120, np.nan, 150, np.nan, 180, 200],
    "customers": [20, 25, 22, np.nan, 30, 35, 40],
    "region": ["seoul", "busan", np.nan, "dauge", "seoul", np.nan, "busan"]
})

# 1-1 결측값 행 전체 삭제
drop_rows = sales_data.dropna()
print(drop_rows)

# 1-2 결측값 열 전체 삭제
drop_cols = sales_data.dropna(axis=1)
print(drop_cols)

# 1-3 특정 열 기준 삭제
drop_sales = sales_data.dropna(subset=["sales"])  # sales열에서 결측값이 있는 기준으로만 삭제
print(drop_sales)

# 2. 평균으로 대체
fill_mean = sales_data.copy()
fill_mean["sales"] = fill_mean["sales"].fillna(
    fill_mean["sales"].mean())  # 평균값으로 결측값 채우기
print(fill_mean)

# 2. 중앙값으로 대체
fill_median = sales_data.copy()
fill_median["sales"] = fill_median["sales"].fillna(
    fill_median["sales"].median())  # 평균값으로 결측값 채우기
print(fill_median)

# 시계열 대체
# 시간 순서가 있는 데이터에서 앞뒤 값으로 결측값을 채운다

# ffill 앞에 값으로 채우기
fill_forward = sales_data.copy()
fill_forward["customers"] = fill_forward["customers"].fillna(method="ffill")
print(fill_forward)

# bfill 앞에 값으로 채우기
fill_backward = sales_data.copy()
fill_backward["customers"] = fill_backward["customers"].fillna(method="bfill")
print(fill_backward)
