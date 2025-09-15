# 실습 1. 튜플 종합연습

# 스텝1 손상된 고객 정보 복원하기

user = ("minji", 25, "Seoul")
user_n = list(user)
user_n[0] = "eunji"
restored_user = tuple(user_n)
print(restored_user)

# 스텝2 고객 정보 언패킹하여 변수에 저장
name, age, city = restored_user
print(f"name:{name},age:{age},city:{city}")

# 스텝3 지역별 보안 정책 분기 처리
if "Seoul" in restored_user:
    print("서울 지역 보안 정책 적용 대상입니다")
else:
    print("일반 지역 보안 정책 적용 대상입니다")

# 스텝4 고객 데이터 통계분석
users = ("minji", "eunji", "soojin", "minji", "minji")
print(users.count("minji"))
print(users.index("soojin"))

# 스텝5 고객 이름 정렬
sorted_users = sorted(users)
print(sorted_users)
