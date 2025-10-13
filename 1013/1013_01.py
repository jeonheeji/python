import pandas as pd

# csv
# comma-seperated values 가장 널리 사용되는 데이터 파일 형식

# 특징
# 쉼표(,)로 값을 구분
# 텍스트 파일이라 어디서나 열람 가능
# 가볍고 빠름
# excel, google sheets 등과 호환


# sample_data 적고 -> 파일 만들기
sample_data = pd.DataFrame({
    "name": ["john", "jane", "park"],
    "age": [25, 30, 35],
    "도시": ["seoul", "busan", "daegu"],
    "salary": [50000, 60000, 55000]
})

# utf-8로 저장 (기본값, 권장)
sample_data.to_csv("sample_data.csv", index=False, encoding="utf-8-sig")

# cp949로 저장 (윈도우 한글)
# sample_data.to_csv("sample_data.csv", index=False, encoding="cp949")
# 읽어올때도 인코딩 어쩌구 적어줘야함
# df = pd.read_csv("sample_data.csv",encoding="cp949")

# 파일 불러와서 읽기
df = pd.read_csv("sample_data.csv")
print(df)
print(f"{df.dtypes}")  # object 데이터 타입확인
print(f"{df.shape}")  # (3,4) 데이터 크키확인

# sep - 구분자 설정 tab으로 구분된 파일 생성
sample_data.to_csv("tab_seperated.txt", sep="\t", index=False)
df_tab = pd.read_csv("tab_seperated.txt", sep='\t')
print(df_tab)
print(df_tab.head)  # 처음 5개 행을 가져옴

# excel
# 특징
# 여러 시트 지원
# 서식, 수식 포함 가능
# 비즈니스에서 가장 많이 사용
# 확장자 .xlsx(최신),.xls(구버전)
# pip install openpyxl 설치해야 가능

# 엑셀파일로 저장하고 불러오기

sample_data = pd.DataFrame({
    "name": ["john", "jane", "park"],
    "age": [25, 30, 35],
    "도시": ["seoul", "busan", "daegu"],
    "salary": [50000, 60000, 55000]
})
sample_data.to_excel("sample_data.xlsx", index=False, sheet_name="default")
print("end")

df_excel = pd.read_excel("sample_data.xlsx")
print(df_excel)

# 여러 시트 다루기 excel 파일로 두개의 시트가 만들어짐
with pd.ExcelWriter("multi_sheet.xlsx") as writer:
    sample_data.to_excel(writer, sheet_name="default1", index=False)
    sample_data["name"].to_excel(writer, sheet_name="name", index=False)
print("end2")

# json으로 !
# javascript object notation
# 웹에서 많이 사용되는 데이터 형식

sample_data = pd.DataFrame({
    "name": ["john", "jane", "park"],
    "age": [25, 30, 35],
    "도시": ["seoul", "busan", "daegu"],
    "salary": [50000, 60000, 55000]
})

sample_data.to_json("sample_data.json", orient="records", indent=2)
print("json")

df_json = pd.read_json("sample_data.json")
print(df_json)
