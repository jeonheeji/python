def get_age_group():
    while True:
        try:
            age = int(input("나이 입력"))
            if age < 0 or age > 150:
                print("Error")
                continue
            break
        except:
            print("숫자로 다시 입력해주세요")

    if age < 20:
        print("미성년자")
    elif age < 40:
        print("청년")
    elif age < 60:
        print("중년")
    else:
        print("노년")


get_age_group()
