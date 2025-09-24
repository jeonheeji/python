
with open('member.txt', 'w', encoding='utf-8')as f:
    for i in range(3):
        user_id = input("id")
        user_pw = input("pw")
        f.write(f"{user_id} {user_pw}\n")

with open('member.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.split()[0])  # 아이디만 출력
        print(line.strip())  # 아이디 + 비밀번호

with open('member.txt', 'r', encoding='utf-8') as f:
    input_id = input("id")
    input_pw = input('pw')
    for line in f:
        user_id, user_pw = line.strip().split()
        if user_id == input_id and user_pw == input_pw:
            print("로그인 성공")
            input_phone = input("전화번호 입력")
            members = {}
            with open('member_tel.txt', 'r', 'utf-8')as f2:

            break
        else:
            print("로그인 실패")
