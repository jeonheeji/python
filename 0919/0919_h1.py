
current_user = None  # 로그아웃


def login(name):
    global current_user
    if current_user is not None:
        print("이미 로그인 되어 있습니다")

    else:
        current_user = name
        print(f"{name}님 로그인 성공!")


def logout():
    global current_user
    print("로그아웃되었습니다")
    current_user = None


login("Ian")
login("CodingOwl")
logout()
login("CodingOwl")
print(current_user)
