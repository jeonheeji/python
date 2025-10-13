import pandas as pd

# 1
practice_data = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["seoul", "busan", "daegu"]
})

practice_data.to_csv("practice.csv", index=False)
df_one = pd.read_csv("practice.csv")
print(df_one)

# 2
korean_data = pd.DataFrame({
    "이름": ["김철수", "이영희", "박민수"],
    "직급": ["사원", "대리", "과장"]
})

korean_data.to_csv("korean.csv", index=False, encoding="utf-8-sig")
df_two = pd.read_csv("korean.csv", encoding="utf-8-sig")
print(df_two)
