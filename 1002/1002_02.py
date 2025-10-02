import pandas as pd


# 인덱싱과 슬라이싱

# 인덱싱
# Series에서 특정 데이터를 선택하는 방법
#  레이블 기반 : 인덱스 이름으로 접근 가능

sales = pd.Series([100, 200, 150, 300, 250], index=[
                  "mon", "tue", "wed", "thu", "fri"], name="daily")
wed_sales = sales["wed"]  # 수요일 인덱스에 있는 값
wed_sales2 = sales.iloc[2]  # 인텍스 숫자로 찾기
wed_sales3 = sales.loc[:"wed"]  # 슬라이싱 -> 여기서는 마지막도 포함!!!!!!!!

selected_days = sales[["mon", "wed"]]  # 월요일, 수요일 값 뽑기

# Boolean 인덱싱
condition = sales >= 200
print(condition)

# 비교 연산자
print(sales[sales == 200])
print(sales[(sales >= 150) & (sales <= 350)])  # 비교연산자 옆으로 괄호로 묶어줘야함 조건!

# 복합조건
weekday_high = sales[(sales >= 200) & (sales.index != "fri")]
print(weekday_high)

# 벡터화 연산
prices = pd.Series([3000, 1500, 4000], index=[
    "ap", "ba", "or"], name="Price")
prices2 = pd.Series([3000, 1500, 4000], index=[
    "ap", "ba", "or"], name="Price")
print(prices+prices2)

# nan 결측값 처리하며 연산하기
# 1. fill_value 사용
price_diff_filled = prices2.sub(prices, fill_value=0)  # 값을 0으로 반환한다는게 아니라
# 동시에 없을 경우 한쪽에 있는 곳에서 불러와서 채워줌
print(price_diff_filled)

# 2. reindex로 먼저 맞추기 fill_value 값으로 넣고 합치기
# 괄호안의 인덱스를 기준으로 reindex 한다!
prices_re = prices.reindex(prices2.index, fill_value=0)
print(prices_re)

# 3. dropna로 결측값 제거 후 연산
price_diff = prices-prices2
price_diff_cleaned = price_diff.dropna()
print("want")
print(price_diff_cleaned)

# 비교 연산
is_b_cheaper = prices > prices2
print(is_b_cheaper)  # 불리언으로 값나옴

# print(prices+500)  # 모든 데이터에 500 추가되서 나옴
# print(prices-1000)  # 뺴기도 가능
# print(prices*0.8)  # 곱하기도 가능
# print(prices/2)  # 나누기도 가능
# 몫, 거듭제곱, 나머지 모두 이렇게 사용가능
