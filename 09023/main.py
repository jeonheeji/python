# 모듈
# 파이썬 코드가 저장된 파일
# 함수, 변수, 클래스 등을 모아놓은 파일로 다른 프로그램에서 가져다 쓸 수 있음

# 코드 재사용 : 한번 작성한 코드를 여러번 사용
# 유지보수 : 기능별로 분리하여 관리가 쉬움
# 협업 : 코드 공유 편리
# 네임스페이스 : 이름 충돌 방지

# 전체 모듈 가져오기
import datetime
import random
import math as m  # 별칭
import calc

result = calc.add(10, 5)
print(result)

# 작성되어있는 모듈


result = calc.add(10, 5)
print(result)
result = calc.subtract(10, 5)
print(result)
result = calc.multiply(10, 5)
print(result)
result = calc.divide(10, 5)
print(result)
result = calc.divide(10, 0)
print(result)
