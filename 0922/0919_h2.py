class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def change_password(self, old_pw, new_pw):
        if self.__password == old_pw:
            self.__password = new_pw
        else:
            return "비밀번호 불일치"

    def check_password(self, password):
        return self.__password == password


user1 = UserAccount("kim", "123")
print(user1.check_password("456")) # False 초기비밀번호 123 != 새로운비밀번호456
print(user1.check_password("123")) # True 
print(user1.change_password("456", "789")) # 비밀번호 불일치
user1.change_password("123", "456") # 비밀번호 일치 -> 456으로 비번바꾸기
print(user1.check_password("456")) # True 
