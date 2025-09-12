# 실습 1. 인덱싱, 슬라이싱 복습문제
# 문제 1. 첫번째 요소와 마지막 요소 출력

nums = [10, 20, 30, 40, 50]
print(nums[0], nums[-1])

# 문제 2. 가운데 세개의 요소 추출하기

nums = [100, 200, 300, 400, 500, 600, 700]
print(nums[2:5])
mid = 7//2
print(nums[mid-1:mid+2])

# 문제 3. 리스트의 원소 두배하기

nums = [1, 2, 3, 4, 5]
for i in range(5):
    nums[i] *= 2

print(nums)

# 문제 4. 리스트 뒤집어서 출력하기

items = ["a", "b", "c", "d", "e"]
print(items[::-1])

# 문제 5. 짝수 인덱스 요소만 출력하기

data = ["zero", "one", "two", "three", "four", "five"]
print(data[::2])

# 문제 6. 슬라이싱으로 리스트 수정하기
movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = ["매트릭스", "타이타닉"]
print(movies)


# 문제 7. 특정 규칙에 따라 요소 추출
subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
subject = subjects[3:8:2]
print(subject)

# 문제 8. 리스트를 3개 구간으로 나누어 역순 병합

data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
data1 = data[:3]
data2 = data[3:6]
data3 = data[6:]
print(data1[::-1], data2[::-1], data3[::-1])


# 실습 2. 리스트 연산 복습문제 (1)
# 문제 1 부분 삭제 후 연결

fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
result = fruits
print(result)

# 문제2 반복리스트 내부요소 삭제
letters = ["A", "B"]
letters *= 3
del letters[2]
print(letters)

# 실습 3. 리스트 주요 메서드 복습문제 (1)
# 문제 1 기차 탑승 시물레이션

train = ["철수", "영희"]
train.extend(["민수", "지훈"])
train.remove("영희")
train.insert(1, "수진")
train.remove("민수")
train.reverse()
print(train)

# 실습 3. 리스트 주요 메서드 복습문제(2)
# 문제 2 숫차처리 게임
number = [5, 3, 7]
number.extend([4, 9])
max_number = max(number)
min_number = min(number)
sum_number = sum(number)
print(max_number, min_number)
print(sum_number)
number.sort()
number.pop()
print(number)
