import pandas as pd

# Data Frame
# pandas의 핵심 자료구조
# 2차원 표 형태의 데이터를 다루는 객체

# 2차원 구조 : 행 열로 구성된 표
# 레이블 기반 : 각 행과 열에 이름 (레이블) 지정 가능
# 각 열마다 다른 데이터 타입 가능

# Data Frame의 구성요소
# 1. 데이터 - 2차원 배열
# 2. 행 인덱스 - 각 행의 레이블
# 3. 열 인덱스
test_data = pd.DataFrame(data=[
    ["kim", 27, "dev", 4500],
    ["lee", 27, "hr", 4800]], index=["01", "02"], columns=["name", "age", "job", "money"])
print(test_data)
