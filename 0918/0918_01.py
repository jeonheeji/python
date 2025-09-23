# 함수
# 특정 작업을 수행하는 코드의 묶음
# 한 번 정의하면 필요할 때마다 호출하여 재사용 가능

# 함수를 사용하는이유
# 코드 재사용성 : 같은 코드 반복 작성할 필요없음
# 모듈화 : 프로그램을 작은 단위로 나누어 관리
# 가독성 향상 : 코드의 의도를 명확히 표현
# 유지보수 용이 : 수정이 필요할 때 함수만 변경
# 추상화 : 복잡한 로직을 단순한 인터페이스로 제공


print('='*20)
print("'첫번쨰 섹션")
print("="*20)
# ...
# 똑같은걸 반복해서 적지 않아도 함수로 사용하면 편리함!

# 함수 정의와 호출
# 함수 정의
# def 함수이릅(매개변수):
# 실행코드
# return 반환값
# 함수 호출
# 결과 = 함수이름(인자)

# 사각형 넓이 구하는 함수


def square(width, height):
    return width*height


print(square(10, 20))

# 실습1. 사칙연산계산기 함수 만들기
# 문제1. 사칙연산 계산기 함수 만들기


def calculate(a, b, operator):

    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return float(a/b)
    else:
        return "지원하지 않는 연산입니다"


a = int(input())
b = int(input())
operator = input()

print(calculate(a, b, operator))


