# 실습 set 종합연습

# 문제1 중복제거 및 개수세기
submissions = ["kim", "lee", "park", 'choi', 'lee', "lee"]
name = set(submissions)
print(f"""제출한 학생 수 : {len(name)}
제출자 명단 : {name}""")

# 문제2 공통 관심사 찾기
user1 = {"SF", "Action", "Drama"}
user2 = {"Drama", "Romance", "Action"}
print(f"""공통 관심 장르 : {user1 & user2}
      서로 다른 장르 : {user1 ^ user2}
      전체 장르 : {user1 | user2}""")

# 문제3 부분집합 관계 판단
my_certificates = {"SQL", "Python", "Linux"}
job_required = {"SQL", "Python"}

print(f"지원 자격 충족 여부 : {my_certificates >= job_required}")
