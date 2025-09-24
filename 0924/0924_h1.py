user1_name, user1_pw = input("이름과 비밀번호를 입력하세요").split(",")
user2_name, user2_pw = input("이름과 비밀번호를 입력하세요").split(",")
user3_name, user3_pw = input("이름과 비밀번호를 입력하세요").split(",")

with open("member.txt", "w", encoding="utf-8") as f:
    f.write(f"user1의 이름 : {user1_name}, user1의 비번 : {user1_pw}\n")
    f.write(f"user2의 이름 : {user2_name}, user1의 비번 : {user2_pw}\n")
    f.write(f"user3의 이름 : {user3_name}, user1의 비번 : {user3_pw}\n")

with open('member.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

name = input("이름을 입력하세요 : ")
pw = input("비밀번호를 입력하세요 : ")

with open("member.txt", "r", encoding='utf-8')as f:
    for line in f:
        if name in line and pw in line:
            print("로그인 성공")
            number = input("전화번호를 입력하세요")
            with open("member_tel.txt", "w", encoding='utf-8') as f2:
                f2.write(f"user의 이름 : {name}, 전화번호 : {number}")
            break
        else:
            print("로그인 실패")
            
