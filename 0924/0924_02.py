# 예외
# 프로그램 실행 중에 발생하는 예상치 못한 상황
# 예외가 발생하면 프로그램이 즉시 멈추지만, 예외 처리를 하면 프로그램을 계속 실행할 수 있습니다

# 오류 vs 예외 의 차이
# 구문 오류(Syntax Error) : 코드를 잘못 작성한 경우
# 프로그램이 시작 못함
# 코드를 수정해야만 해결가능함
# print("hello" -> 구문오류 문법상 오류

# 예외 : 문법은 맞지만 실행 중 발생하는 문제
# 프로그램 실행 중 발생
# try - except로 처리가능
# result = 10/n -> n=0 예외발생

# 예외 처리가 필요한 경우
age = int(input("나이를 입력해주세요 : "))

# 예외 처리
while True:
    try:
        age = int(input("나이 입력"))
        break
    except:
        print("숫자로 입력해주세요")

# try 블록은 최소한으로
try:
    name=input("이름 :") # 오류가 안날 불필요한 것들을 넣을 필요없음
    age=input("나이 :")
    print(f"{name} {age}")
except:
    print("오류")
