# 실습3. 나이에 따른 영화 관람가능

age = int(input("나이를 입력해주세요 :"))

if age <= 12:
    print("전체 관람가")
elif age <= 15:
    print("12세 이상 관람가")
elif age <= 18:
    print("15세 이상 관람가")
else:
    print("청소년 관람불가 가능")
