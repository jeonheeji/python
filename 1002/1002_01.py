import pandas as pd


# Series
# 1. 차원배열
# 2. 레이블(인덱스) 보유
# 3. 동일 타입 : 하나의 series 안의 모든 데이터는 같은 타입

tem_list = [15.5, 17.2, 18.9, 19.1, 20.1]
tem = pd.Series(tem_list, name="4월_기온")
print(tem)
date = pd.date_range("2025-04-01", periods=5)
print(date)

# Series=Value(값)+Index(인덱스)+Name(이름)
data_se = pd.Series(data=[10, 20, 30, 40, 50], index=[
                    "A", "B", "C", "D", "E"], name="score")
print(data_se)

# 각 구성요소의 역할
# Value(값) : 실제 데이터가 저장되는 부분 Numpy로 저장 빠른 수치연산 가능
# Index(인덱스) : 각 값을 식별하는 레이블 사용자 정의 가능
# Name(이름) : 전체를 설명하는 이름 선택사항(없어도됨) DataFrame 결합 시 컬럼명이 됨

int_series = pd.Series([1, 2, 3, 4, 5])
print(f"Integer Series dtype: {int_series} ")

# 여러개 섞이면 전체를 잘 설명할 수 있는걸로 자동 변환
# dtype 중요한이유
# 메모리사용량 결정 / 연산 가능 여부 / 성능에 영향

# 인덱스 넣는 방법 원하는 인덱스 사용가능
tem_date = pd.Series(tem_list, index=date, name="april")
print(tem_date)

# 딕셔너리로 인덱스와 값을 넣을 수 이씀
product = {
    "노트북": 15,
    "마우스": 40,
    "키보드": 20
}
pro_se = pd.Series(product, name="now")
print(pro_se)


# scalar 모든값을 0으로 넣기
scalar_se = pd.Series(0, index=["월", "화", "수", "목"], name="판매량")
print(scalar_se)

# 속성알아보기
test_scores = pd.Series(data=[85, 86, 59, 97], index=[
                        "k", "l", "p", "j"], name="score")
print(test_scores.values)  # [85,86,59,97] data 값
print(test_scores.index)  # index의 값과 index dtype
print(test_scores.name)  # score name으로 지정해준값
print(test_scores.dtype)  # int64 데이터의 타입
print(test_scores.shape)  # (4,) 모양
print(test_scores.size)  # 4 크기
print(test_scores.ndim)


# 연습문제
# 문제1
pro1 = pd.Series([5, 10, 15, 20])
print(pro1)

# 문제2
pro2 = pd.Series([90, 80, 85, 70], index=["국어", "영어", "수학", "과학"])
print(pro2)

# 문제3
pro3_dic = {
    "서울": 950,
    "부산": 340,
    "인천": 520
}
pro3 = pd.Series(pro3_dic)
print(pro3["인천"])

# 문제4
pro4 = pd.Series([1, 2, 3, 4])
print(pro4.dtype)

# 문제5
s1 = pd.Series([3, 5, 7], index=["a", "b", "c"])
s2 = pd.Series([10, 20, 30], index=["b", "c", "d"])
print(s1+s2)

# 문제6
pro6 = pd.Series([1, 2, 3, 4, 5])
print(pro6+10)
