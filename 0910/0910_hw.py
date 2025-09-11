# 실습 1. 영화정보 출력하기

title = "Inception"
director = "Christopher Nolan"
year = 2010
genre = "Sci-Fi"

print(f'Title: {title} Director: {director} Year: {year} Genre: {genre} ')


# 실습 2. 자기소개하기

name = "전희지"
age = 28
mbti = "istp"

print(f"안녕하세요\n제 이름은 {name}이고,\n{age}살입니다.\n제 MBTI는 {mbti}에요.\n")


# 실습 3. 대학생의 용돈관리

seed_money = 300000
seed_money -= 80000
seed_money -= 9000*5
seed_money += 120000
seed_money *= 1.2
seed_money *= 2/3

print(seed_money)

# 실습 4. EDM 리듬 트랙 만들기
intro = "둠칫"
drop = "두둠칫"


print(intro+drop*3)


# 실습 5. input 연습하기
name = input("이름을 입력하세요 : ")
age = input("나이를 입력하세요 : ")

print(f"안녕하세요. 저는 [{name}]이고, [{age}]살입니다 ")

# 실습 6. 입력과 연산 연습하기 -1 넓이둘레

width = int(input("가로: "))
lenth = int(input("세로: "))

print(f"""넓이: {width*lenth}
둘레: {2*(width+lenth)}""")

# 실습 6-2. 네자리수 입력 받고 각 자리수 분리하여 출력

number1, number2, number3, number4 = input("네자리 정수를 입력하세요 :").split()
print(f"""천의 자리: {number1}
백의 자리: {number2}
십의 자리: {number3}
일의 자리: {number4}""")

number = int(input("네자리수 정수를 입력하세요 : "))
print(f"천의자리 : {number//1000}")
number %= 1000
print(f"백의자리 : {number//100}")
number %= 100
print(f"십의자리 : {number//10}")
number %= 10
print(f"일의자리 : {number}")


# 실습 7. 발표 순서와 발표 주제 정하기

name1, name2, name3 = input("발표자 이름 3명을 입력하세요: ").split()
subject1, subject2, subject3 = input("발표 주제 3개를 입력하세요: ").split()


print(f"""📢 발표 순서 안내입니다
1조 발표자: {name1} - 주제: {subject1}
2조 발표자: {name2} - 주제: {subject2}
3조 발표자: {name3} - 주제: {subject3}""")


# 실습 8. 날짜와 시간

year, month, day = input("년,월,일을 입력해주세요 : ").split()
print(year, month, day, sep=".")
# sep 구분자 사용하는거 외워두기!!!!! .으로 구분함
hour, minute, second = input("시,분,초를 입력해주세요: ").split()
print(hour, minute, second, sep=":")
# sep 구분자 사용하는거 외워두기!!!! :으로 구분함

year, month, day = input("년,월,일을 입력해주세요 : ").split('.')
print(year, month, day)
# split 안에다가 구분자 넣어둠
hour, minute, second = input("시,분,초를 입력해주세요: ").split(':')
print(hour, minute, second)
# split 안에다가 구분자 넣어둠


print(f"""RE4의 개강일은 {year}년 {month}월 {day}일
시작 시간은 {hour}시 {minute}분 {second}입니다.""")
