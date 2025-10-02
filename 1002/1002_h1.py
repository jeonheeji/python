import pandas as pd
# 실습 2
# 문제 1
pro1 = pd.DataFrame([['홍길동', 28, "서울"], ["김철수", 33, "부산"], ["이영희", 25, "대구"]],
                    index=[0, 1, 2], columns=["이름", "나이", "도시"])
print(pro1)

# 문제2
pro2 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(pro2)

# 문제3
pro3 = pd.DataFrame(
    [{"과목": "수학", "점수": 90}, {"과목": "영어", "점수": 98}, {"과목": "과학", "점수": 95}])
print(pro3)

# 문제4
pro4 = pd.DataFrame({"이름": ["민수", "영희", "철수"], "점수": [
                    80, 92, 77]}, index=["학생1", "학생2", "학생3"])
print(pro4)

# 문제5
kor = pd.Series([90, 85, 80], index=["a", "b", "c"])
eng = pd.Series([95, 88, 82], index=["a", "b", "c"])
pro5 = pd.DataFrame({"col1": kor, "col2": eng})
print(pro5)

# 문제6
pro6 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(pro6[["B", "A"]])

# 문제7
pro7 = pd.DataFrame([["펜", 1000, 50], ["노트", 2000, 30]],
                    index=[0, 1], columns=["produce", "price", "stock"])
print(pro7)

# 문제8
pro8 = pd.DataFrame({"국가": ["한국", "일본", "미국"], "수도": ["서울", "도쿄", "워싱턴"]})
print(pro8[["국가"]])
