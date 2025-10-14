import pandas as pd
# 1
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charile", "David"],
    "score": [88, 95, 70, 100]
})
df_s = df.sort_values(by="score")
print(df_s)
df_s = df.sort_values(by="score", ascending=False, ignore_index=True)
print(df_s)

# 2
df = pd.DataFrame({
    "이름": ["가", "나", "다", "라", "마"],
    "반": [2, 1, 1, 2, 1],
    "점수": [90, 85, 80, 95, 85]
})
df_s = df.sort_values(by=["반", "점수"], ascending=[True, False])
print(df_s)
df_i = df_s.sort_index(axis=1)
print(df_i)

# 3
df = pd.DataFrame({
    'value': [10, 20, 30, 40],
}, index=[3, 1, 4, 2])
df_i = df.sort_index()
print(df_i)
df_1 = df.sort_index(ascending=False)
print(df_1)
df_2 = df.sort_values(by="value")
print(df_2)
