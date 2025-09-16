# set
# 중복되지 않은 요소들의 순서가 없는 집합
# 수학의 집합 개념을 구현
# 해시 테이블 기반으로 빠른 멤버십 테스트 가능

# WHY?
# 중복제거 필요한 경우
visitors = ["철수", "영희", "철수", "민수", "영희", "철수"]

# 리스트로 중복 제거 (비효율적)
unique_visitors_list = []
for visitor in visitors:
    if visitor not in unique_visitors_list:
        unique_visitors_list.append(visitor)
print(unique_visitors_list)

# set으로 중복제거
unique_visitor_set = set(visitors)
print(unique_visitor_set)

# se의 특싱
# 1. 순서없음 : 요소들의 순서 x 인덱싱 슬라이싱 불가
# 2. 중복불가
# 3. 변경가능 추가 삭제 가능
# 4. 빠른 검색 0(1)시간 복잡도로 요소 확인

# set 생성 방법
# 1. 빈 set 생성
empty_set = set()  # {} 사용 불가 dicn 이라서

# 2. 값이 있음
numbers = {1, 2, 3, 5, 4, 3, 2, 4}
print(numbers)  # {1,2,3,4,5} 중복 제거

# 3. 리스트/ 튜플 -> set
list_numbers = [1, 2, 3, 3, 5, 6, 7]
set_numbers = set(list_numbers)  # {1,2,3,5,6,7}

# 4. 문자열에서 set 생성
chars = set("hello")
print(chars)  # {h,e,l,o}

# comprehension
for i in range(10):
    print(i)

com_set = {i for i in range(10)}
print(com_set)


com_list = [i for i in range(2, 10, 2)]
print(com_list)

# set에 저장가능한 데이터 타입
# hashable 타입만 가능(불변타임)
valid_set = {1, "문자열", (1, 2), 3.14, True}
# 가변타입은 x 리스트, dictionary
# 중첩 set을 만들려면 frozenset() 사용
nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(nested_set)

# set 메서드

colors = {"빨강", "노랑", "파랑"}
colors.add("초록")  # 초록 추가

colors.update(["보라", "주황"])  # 보라, 주황 추가됨

colors.remove("보라")  # 보라 사라짐
# colors.remove("검정") # 에러남 검정없는데 검정삭제해서
colors.discard("검정")  # 없어도 에러안남 걍 삭제완료

popped = colors.pop()
print(popped)  # 순서대로가 아닌 랜덤으로 삭제

colors.clear()
print(colors)  # 내부요소 모두 삭제

# 집합연산
A = {1, 2, 3, 4, 5}
B = {1, 2, 6, 7, 8}

# 교집합
intersection1 = A & B
intersection2 = A.intersection(B)
print(intersection1, intersection2)

# 합집합
union1 = A | B
union2 = A.union(B)
print(union1, union2)

# 차집합
difference1 = A-B
difference2 = A.difference(B)
print(difference1, difference2)

# 대칭차집합
sym_difference1 = A ^ B
sym_difference2 = A.symmetric_difference(B)
print(sym_difference1, sym_difference2)

a = {1, 2, 3}
b = {3, 4, 5}
a.intersection_update(b)  # a를 교집합으로 업데이트 하겠다 {3}으로 변한다

a = {1, 2, 3}
a.difference_update(b)  # {1,2} 차집합으로 업데이트 됨

a = {1, 2, 3}
a.symmetric_difference_update(b)  # 대칭차집합으로 업데이트 됨

a = {1, 2, 3}
a.update(b)  # union 없이 합집합으로 업데이트
a |= b

# 집합 관계 확인
# 부분집합, 상위집합

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {6, 7, 8}

# 부분집합확인 논리 연산자로 비교도 가능
print(a.issubset(b))  # a가 b의 부분집합인가요? true

# 상위집합인지
print(a.issuperset(b))  # a는 b의 상위집합인가요? false

# 서로수집합
print(a.isdisjoint(c))  # a와 c는 서로수 집합이니? true

# frozenset() = 불변집합
fs1 = frozenset([1, 2, 3, 3, 4])
# fs1.add 불가능 불변이니께,, 수정 불가하다
