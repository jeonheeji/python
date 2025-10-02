# 통계함수
import pandas as pd

daily_sales = pd.Series([111, 222, 333, 444, 555,
                         666, 777, 888, 999, 112, 113,
                         114, 115, 116, 111, 2, 3,
                         4, 5, 6, 7, 8,
                         9, 10, 11, 12, 13,
                         14, 15, 16, 17, 18], index=pd.date_range("2025-09-01", periods=32), name="Sales")
mean_value = daily_sales.mean()
print(f"{mean_value:.2f}")

# mode 최빈값
mode_value = daily_sales.mode()
print(f"{mode_value}")

# 산포도 측정
# 데이터가 얼마나 퍼져있는지 알려주는 통계량

max_value = daily_sales.max()
min_value = daily_sales.min()
print(max_value, min_value)

# 범위 (range) : 최댓값 - 최솟값
range_value = max_value-min_value
print(range_value)

# 분산 (var) : 평균으로부터 떨어진 정도의 제곱의 평균
variance = daily_sales.var()
print(variance)

# 표준편차 : 분산의 제곱근
std_dev = daily_sales.std()
print(std_dev)
