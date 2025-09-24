def safe_get(lst, index, default=None):
    while True:
        try:
            return lst[index]
        except IndexError:
            return default

    # 테스트
numbers = [10, 20, 30]
print(safe_get(numbers, 1))
print(safe_get(numbers, 10))
print(safe_get(numbers, 10, -1))
