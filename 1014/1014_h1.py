import pandas as pd

df = pd.DataFrame({
    "이름": ["민준", "서연", "지후", "서준", "지민"],
    "점수": [78, 92, 85, 60, 88],
    "반": [1, 2, 1, 2, 1]
})

df1 = df[df["점수"] >= 80]
print(df1)

df2 = df[(df["반"] == 1) & (df["점수"] >= 85)]
print(df2)

df3 = df[(df["이름"] == "서연") | (df["이름"] == "지민")]
print(df3)

df4 = df3.reset_index(drop=True)
print(df4)

df5 = df[(df["점수"] <= 80) | (df["반"] == 2)]
print(df5)

df6 = df5[df5["점수"] >= 70]
df6.reset_index(drop=True)
print(df6)
