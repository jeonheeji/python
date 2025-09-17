# 실습 4. 리스트 컴프리 헨션 연습문제
# 문제1. 제곱값 리스트 만들기

double = [x**2 for x in range(1, 11)]
print(double)

# 문제2. 3의 배수만
triple = [x for x in range(1, 51) if x % 3 == 0]
print(triple)

# 문제3. 길이 5이상 단어만
fruits = ["apple", 'fig', 'banana', 'plum', 'cherry', 'pear', 'orange']
fruit = [x for x in fruits if len(x) >= 5]
print(fruit)
