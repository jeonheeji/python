import pandas as pd
import numpy as np
# 1
df = pd.DataFrame({
    "이름": ["김철수", "이영희", "박민수"],
    "국어": [90, 80, 70]
})

one = pd.DataFrame({"수학": [95, 100, 88]})
df = pd.concat([df, one], axis=1)
print(df)
df2 = df.drop("이름", axis=1)
print(df2)

# 2
df = pd.DataFrame({
    "제품": ["A", "B"],
    "가격": [1000, 2000]
})
two = pd.DataFrame([{"제품": "C", "가격": 1500}])
df = pd.concat([df, two], ignore_index=True)
print(df)
df2 = df.drop(0)
print(df2)

# 3
df = pd.DataFrame({
    "과목": ["국어", "영어", "수학"],
    "점수": [85, 90, 78]
})
df = df.drop(df[df["점수"] < 80].index)
print(df)
df["학년"] = 1
print(df)

# 4
df = pd.DataFrame({
    "이름": ["A", "B"],
    "나이": [20, 22]
})
four = pd.DataFrame([{"이름": "C", "나이": 25, "키": np.nan}])
df = pd.concat([df, four])
print(df)

# 5
df = pd.DataFrame({
    "부서": ["영업", "기획", "개발", "디자인"],
    "인원": [3, 2, 5, 1]
})
df = df.drop(df[df["인원"] <= 2].index)
df["평가"] = "미정"
print(df)
