list1 = list()

list2 = list("hello")

print(list1)
print(list2)

print(list2[0])  # index는 0부터 시작 = 첫번째글자

# h  e  l  l  o
# 0  1  2  3  4
# 0 -4 -3 -2 -1

# list[a:b] = a부터 b-1까지
# list[a:b:c] = a부터 b-1까지 c칸의 간격을 두고

numbers = [10, 20, 30, 40]
print(numbers[1:3])  # [20,30]
print(numbers[::-1])  # 뒤집혀서

list1 = [10, 20, 30, 40, 50]

del list1[3]  # 3번째 인덱스 40 제거
print(list1)

del list1[1:3]
print(list1)  # 20,30 삭제

del list1
# print(list1)  # 에러 !

# 요소 추가 메서드
numbers = [10, 21, 15, 22, 54]

numbers.append(20)

print(numbers)  # 마지막에 20 추가돼 (append는 하나만!)

numbers.append(12)

numbers.extend([19, 31])  # 여러요소를 맨뒤에 적을 수 있음

print(numbers)

numbers.insert(2, 30)
print(numbers)  # 원하는 위치에 원하는 값 넣을 수 있음

# append & extend 차이점
# append - 리스트 자체가 추가됨
# extend - 리스트안의 요소들이 추가됨!

# 삭제 메서드

fruits = ["사과", "바나나", "오렌지", "바나나", "포도"]
fruits.remove("바나나")
print(fruits)  # 앞에있는거 하나만 삭제

removed = fruits.pop()  # pop() 맨 마지막 삭제
print(removed)

removed = fruits.pop(1)  # 인덱스 1번이 삭제
print(fruits)

fruits.clear()  # 모든요소 삭제 but 변수는 사라지지않음 즉 fruits 안에있는게 사라지고 fruits 변수명은 살아있음

# 요소 검색, 정렬 메서드

numbers = [1, 2, 6, 9, 5, 3, 2, 4, 7]

idx = numbers.index(6)
print(idx)  # 몇번째 요소에 6이 들어가 있는지

count = numbers.count(2)
print(count)  # 2라는 숫자가 몇개 들어가 있는지

numbers.sort()
print(numbers)  # 오름차순 (reverse=True) -> 내림차순

# sorted -> 원본값은 그대로
original = [3, 2, 5, 7, 1]
sorted_list = sorted(original)
sorted_list = sorted(original, reverse=True)  # 내림차순

print(original)
print(sorted_list)

# 연산 메서드
numbers = [5, 2, 7, 3, 11, 45]
max_num = max(numbers)
min_num = min(numbers)
sum_num = sum(numbers)
print(max_num, min_num, sum_num)
