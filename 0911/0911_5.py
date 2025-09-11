# 실습5. 편의점 도시락 구매하기

kim = 2500
sam = 1500
do = 4000

money = int(input("금액을 입력하세요"))
name = input("원하는 상품을 입력하세요")
if name == "kim":
    if money >= kim:
        print("구매에 성공했습니다")
    else:
        print("금액이 부족합니다")
if name == "sam":
    if money >= sam:
        print("구매에 성공했습니다")
    else:
        print("금액이 부족합니다")
if name == "do":
    if money >= do:
        print("구매에 성공했습니다")
    else:
        print("금액이 부족합니다")
