import pandas as pd
import numpy as np
# 그룹화의 집계

# GroupBy
# 데이터를 특정 기준에 따라 묶어서 분석하는 것
# 전체 평균만으로는 부족한 경우가 많음
# 카테고리별, 기간별로 나누어 보면 숨겨진 패턴 발견 가능
# 세그먼트별 비교 분석 가능

employee_data = pd.DataFrame({
    "name": ["alice", "bob", "charlie", "david", "eve", "frank", "grace", "henry"],
    "department": ["dev", "dev", "sales", "sales", "dev", "hr", "hr", "sales"],
    "years": [3, 5, 2, 7, 10, 4, 6, 3],
    "salary": [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]
})
dept_avg = employee_data.groupby("department")["salary"].mean()
print(dept_avg)
