import pandas as pd
# 1
df = pd.DataFrame({
    "grade": [1, 2, 1, 2, 1, 3],
    "name": ["kim", "lee", "park", "choi", "jung", "han"],
    "kor": [85, 78, 90, 92, 80, 75]
})
print(df.groupby("grade")["kor"].mean())

# 2
df = pd.DataFrame({
    "class": [1, 1, 1, 2, 2, 2],
    "subject": ["math", "math", "eng", "math", "eng", "eng"],
    "score": [80, 90, 85, 70, 95, 50]
})
print(df.groupby(["class", "subject"])["score"].count())
print(df.groupby(["class", "subject"])["score"].mean())
print(df.groupby(["class", "subject"])["score"].agg(["count", "mean"]))
df.rename(columns={"mean": "avg"}, inplace=True)  # 나중에 이런식으로 열이름 바꿀수 있음!

# 3
df = pd.DataFrame({
    "region": ["seoul", "seoul", "busan", "busan", "daegu"],
    "seller": ["A", "B", "A", "B", "A"],
    "sales": [100, 200, 150, 120, 130]
})
print(df.groupby(["region", "seller"])["sales"].agg(["sum", "max"]))

# 4
df = pd.DataFrame({
    "team": ["A", "A", "B", "B", "A", "B"],
    "position": ["fw", "df", "fw", "df", "df", "fw"],
    "score": [3, 2, None, 1, 4, 2]
})
print(df.groupby(["team", "position"], dropna=False)["score"].mean())

# 5
df = pd.DataFrame({
    "dept": ["hr", "hr", "it", "it", "sales", "sales"],
    "gender": ["m", "f", "f", "m", "f", "f"],
    "salary": [3500, 3200, 4000, 4200, 3000, 3100]
})
print(df.groupby(["dept", "gender"])["salary"].agg(["count", "sum"]))
