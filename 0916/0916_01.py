import copy
# 딕셔너리
# Key - Value 쌍으로 데이터를 저장하는 자료구조
# 해시 테이블 기반으로 매우 빠른 검색 속도
# Python의 가장 강력하고 유용한 자료구조 중 하나

# dict x -> 두개의 리스트로 관리
student_ids = ["20230001", "20230002", "20230003"]
student_names = ["김철수", "이영희", "박민수"]

# 특정 학번의 이름을 찾을려면? 0(n) 시간걸림
target_id = "20230002"
if target_id in student_ids:
    index = student_ids.index(target_id)
    name = student_names[index]
    print(name)

# 딕셔너리 사용하는경우
students = {
    "20230001": "김철수",
    "20230002": "이영희",
    "20230003": "박민수"
}
print(students["20230002"])  # 0(1) - 즉시 접근

# 특징
# Key - Value 쌍 : 각 값에 고유한 키로 접근
# 빠른 검색 : 0(1) 시간 복잡도
# 변경가능 : 요소 추가, 수정, 삭제 가능
# Key는 유일 : 중복 키 불가 (값은 중복 가능)
# 순서보장 -> 시퀀스는 아님!

# Dictionary 생성
# 1. 빈 dic 생성
empty_dict = {}  # dict
empty_set = set()

# 2. 값 존재
person = {
    "name": "김철수",
    "age": "25",
    "city": "Seoul"
}

# 3. dict() 생성자 사용
person2 = dict(name="이영희", age=25, city="Seoul")  # key는 변수명 정해주듯이! "" 없이

# 4. 리스트나 튜플로 생성하기 상관없이 다돼
pairs = [("a", 1), ("b", 2)]
dict_from_pairs = dict(pairs)  # dict형태로 바뀜

# 5. zip()
keys = ["name", "age", "city"]
values = ["박민수", 21, "대전"]
person3 = dict(zip(keys, values))

# 6. dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}  # {1:1,2:4,3:9,4:16,5:25}

# 7. fromkeys() 메서드
keys = ["a", 'b', 'c']
default_dict = dict.fromkeys(keys, 0)  # 모든 값이 0으로 들어감 - 초기화

# 8. Key로 사용가능한 타입
# Hashable 타입만 Key로 사용가능
valid_dict = {
    1: '정수',
    3.14: '실수',
    '문자열': 'string',
    (1, 2): "튜플",
    True: '불리언',
    frozenset([1, 2]): 'frozenset'
}

# UnHashable 타입은 불가
# 리스트, set, 딕셔너리 -> Key 값으로 사용불가

# 접근과 수정
student = {
    'name': '김철수',
    'age': 20,
    'major': '컴퓨터공학',
    'gpa': 3.7
}

# 1. 대괄호 표기법(KeyError 위험)
name = student["name"]  # 김철수
# grade=student["grade"] # KeyError -> dict안에 없는 키를 찾고 싶기 떄문

# 2. get()으로 사용 안전!!
major = student.get("major")  # 컴퓨터공학
grade = student.get("grade")  # none 에러나지 않고 none으로 뜸
grade2 = student.get("grade", 'n/a')  # 없으면 n/a 출력

# keys(),values(),items()
print(student.keys(), list(student.keys()))  # 키만출력 , list로 형변환 후 출력
print(student.values())  # 값만출력
print(student.items())  # 다출력

# 값 수정, 추가
student = {
    'name': '김철수',
    'age': 20,
    'major': '컴퓨터공학',
    'gpa': 3.7
}
student["age"] = 23  # 23으로 나이 수정

student["grade"] = 3  # grade:3을 추가!

# update() 여러개 한번에!
student.update({
    'gpa': 4.0,
    "city": "Seoul",
    'email': '123@gmail.com'
})  # 한번에 수정 추가 가능!!

info_dict = {'age': 22, 'grade': 1, 'phone': '010-1234-1234'}
student.update(info_dict)
print(student)

# 삭제
# del student[grade]  # key와 value 쌍으로 삭제
# popped = student.pop()  # 사용불가능함,,,, 마지막이라고 순서가 있어 보이는거지 순서가 없음
popped = student.pop('phone')  # 원하는 값을 넣어줘야함!
last_item = student.popitem()  # 마지막 항목 지울때는 popitem !
student.clear()  # 안에 있는 모든 요소 삭제

# 중요 메서드들
scores = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78
}
# setdefault 없으면 추가 있으면 기존 반환
scores.setdefault('정수진', 88)  # 원하는 항목을 넣을 수 있음
scores.setdefault("김철수", 100)  # 원래 있던 값은 수정이 안돼 기존값 유지

# copy 얕은 복사
scores_copy = scores.copy()
scores_copy["최동훈"] = 95  # scores를 복사해서 최동훈이라는 걸 넣어줌

# 맨윗줄에 import copy
# deepcopy() 깊은 복사
nested_dict = {
    "time1": {"leader": '김철수', 'members': ['이영희', '박민수']},
    "time2": {"leader": '정수진', 'members': ['최동훈', '강미나']}
}
shallow = nested_dict.copy()  # 얕은
deep = copy.deepcopy(nested_dict)  # 깊은

# 원본 값에 추가
nested_dict['time1']['members'].append('신입')
print(shallow["time1"]["members"])  # 신입복사됨 ㅋ
print(deep["time1"]["members"])  # 신입복사 안돼

# 키만 순회(기본)
for name in scores:
    print(f'{name}: {scores[name]}')

for name in scores.keys():
    print(f'{name}: {scores[name]}')

for value in scores.values():
    print(f'{value}')

# 평균 값 계산
average = sum(scores.values())/len(scores)
print(average)

# 키 - 값 쌍순회
for key, value in scores.items():
    print(f'{key}:{value}')

for idx, (key, value) in enumerate(scores.items(), 1):
    print(f"{idx}번쨰 {key}:{value}")
