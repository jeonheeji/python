# 실습 4. 시,분,초 구하기

time = int(input())

if time >= 3600:
    hour = time//3600
    minute = time//60
    second = time % 60
    print(f"{hour}시 {minute}분 {second}초")
elif time >= 60:
    minute = time//60
    second = time % 60
    print(f"{minute}분 {second}초")
else:
    second = time
    print(f"{second}초")


time = int(input())
hour = time//3600
minute = (time % 3600)//60
second = time % 60

if hour > 0:
    print(f"{hour}시 {minute}분 {second}초")
elif minute > 0:
    print(f"{minute}분 {second}초")
else:
    print(f"{second}초")
