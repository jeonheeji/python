# 접근 제어자
# 객체 지향 프로그래밍에서 클래스의 멤버(속성, 메서드)에 대한 접근 권한을 제어하는 메커니즘


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        # 외부에서 자유롭게 호출가능
        self.speed += amount
        return f"속도가 {self.speed}"  # public method

    def get_info(self):
        return f"{self.brand}{self.model}"


car = Car("tesla", "model3")
print(car.model)  # 정상접근
print(car.brand)
print(car.get_info())  # 정상호출
car.speed = 200  # 직접 수정가능

# Private 속성/ 메서드 (언더스코어 2개__)


class SecuritySystem:
    def __init__(self, password):
        self.__password = password  # Private 속성
        self.__security_level = "high"
        self.__failed_attempts = 0

    def __encrypt_password(self, pwd):  # Private 메서트 내부적으로만 사용
        return pwd[::1] + "encrypted"

    def __check_security(self):
        return self.__failed_attempts < 3

    def authenticate(self, password):
        if not self.__check_security():
            return "계정이 잠겼습니다"
        encrypted = self.__encrypt_password(password)

        if encrypted == self.__encrypt_password(self.__password):
            self.__failed_attempts = 0
            return "인증성공"
        else:
            self.__failed_attempts += 1
            return "인증실패"


security = SecuritySystem("123")
print(security.authenticate("wrong"))
print(security.authenticate("123"))

print(security._SecuritySystem__password)  # 권장하지 않음

# print(security.__password) 클래스 내부에서만 사용가능!
# security.__check_security()


# propety를 사용하지 않은 경우

class Circle1:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14*self.radius**2

    def set_radius(self, radius):
        self.radius = radius

# propety를 사용한 경우


class Circle2:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):  # 메서드로 접근
        return 3.14*self.__radius**2

    @radius.setter
    def radius(self, radius):
        self.__radius = radius


c1 = Circle1(5)
print(c1.get_area())  # 괄호있이!
c1.set_radius(10)
print(c1.get_area())

c2 = Circle2(4)
print(c2.radius)  # Propety는 소괄호 필요없음 / 속성 접근
c2.radius = 10
print(c2.radius)
