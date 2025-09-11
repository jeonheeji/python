# 구구단만들기 4단만
for i in range(1, 10, 1):
    print(f"4X{i}={4*i}")

# 구구단 전체
for i in range(1, 10):
    print(f"{i}단")
    for j in range(1, 10):
        print(f"{i}x{j}={i*j}")
    print("=========")


# 별 패턴 1: 직각삼각형

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# 정사각형 만들기

for i in range(1, 6):
    print("*****", end="\n")
