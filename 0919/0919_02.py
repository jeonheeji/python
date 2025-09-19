# 재귀함수
# 자기 자신을 호출하는 함수

# 팩도리얼 계산(n!)

def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)


print(factorial(5))

# 피보나치 수열
# 0 1 1 2 3 5 8 13...

# n항까지의 피보나치 수열


def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1)+fibo(n-2)


for i in range(10):
    print(fibo(i))
print()

# 거듭제곱 구하기


def power(a, b):
    if b == 0:
        return 1
    return a*power(a, b-1)


print(power(2, 3))

# 1부터 n까지의 합


def sum_to_n(n):
    if n <= 1:
        return 1
    return n+sum_to_n(n-1)


print(sum_to_n(5))

# 문자열 뒤집기


def reverse_string(s, n):
    if len(s) == 0:
        return ""
    return s[-1]+reverse_string(s[:-1])


"""h e l l o
o reverse_string 
o l rever list 
o l l reber
o l l e return
o l l e h"""

print(reverse_string("hello"))
