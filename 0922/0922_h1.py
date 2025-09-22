class User:
    total_users = 0

    def __init__(self, username):
        self.username = username
        self.points = 0
        User.total_users += 1  # 클래스 변수 업데이트

    def add_points(self, amount):
        self.points += amount

    def get_level(self):
        if self.points < 100:
            return "bronze"
        elif self.points < 500:
            return "silver"
        elif self.points >= 500:
            return "Gold"

    @classmethod
    def get_total_users(cls):
        print(f"{cls.total_users}명 입니다")


user1 = User("김철수")
user2 = User("이영희")
User.get_total_users()
user1.add_points(200)
print(user1.get_level())
