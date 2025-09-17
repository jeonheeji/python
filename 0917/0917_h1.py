# 문제 1 구구단만들기
for i in range(1, 10):
    print(f"{i}단")
    for j in range(1, 10):
        print(f"{i}X{j}={j*i}")

# 문제2 중첩 for문 별찍기
n1 = int(input("몇 줄? ",))

for i in range(1, n1+1):
    for j in range(i):
        print("*", end="")
    print()


n2 = int(input("몇 줄?",))

for i in range(1, n2+1):
    for j in range(n2-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    for j in range(n2-i):
        print(" ", end="")

    print()


n3 = int(input("몇 줄? ",))

for i in range(1, n3+1):
    for j in range(n3-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
