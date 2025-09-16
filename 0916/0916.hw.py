# 딕셔너리 종합 연습 문제
# 문제1. 딕셔너리 핵심 개념 통합 실습
user = {}
keys = ['username', 'email', 'level']
values = ['skywalker', 'sky@example.com', '5']
user = dict(zip(keys, values))

email_value = user["email"]
user['level'] = 6

problem5 = user.get('phone', "미입력")
print(problem5)

user.update({"nickname": "sky"})
del user["email"]
user.setdefault("signup_date", "2025-07-10")

print(user)

# 문제2. 학생점수 관리
students = {}
students.update({
    "Alice": 85,
    "Bob": 90,
    "Charlie": 95

})
students.update({"David": 80})
students["Alice"] = 88
del students["Bob"]
print(students)
