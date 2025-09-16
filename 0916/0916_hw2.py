# for문 기본 문법 문제

# 문제1 리스트의 값 두 배로 변환
numbers = [3, 6, 1, 8, 4]
for i in range(len(numbers)):
    numbers[i] *= 2
print(numbers)

# 문제2 문자열의 길이 구해서 새 리스트 만들기
words = ["apple", "banana", "kiwi", "grape"]
lenth = []
for i in range(len(words)):
    lenth.append(len(words[i]))
print(lenth)

# 문제3 좌표 튜플에서 x,y좌표 나누기
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
x_values = []
y_values = []
for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)
print(x_values, y_values)
