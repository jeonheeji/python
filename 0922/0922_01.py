# 클래스
# 클래스 = 붕어빵 틀 / 객체(인스턴스) = 실제로 만들어진 붕어빵
# 관련된 데이터와 기능을 하나로 묶어서 관리가능

# class 클래스 이름:
# def __init__(self):
# pass


# def 메서드이름(self):
# pass


class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, increase):
        self.speed = min(150, self.speed+increase)
        print(f"속도가 {increase}km/h 증가 했습니다. 현재 속도는 {self.speed}")

    def brake(self, decrease):
        self.speed = max(0, self.speed-decrease)
        print(f"속도가 {decrease}km/h 증가 했습니다. 현재 속도는 {self.speed}")

    def info(self):
        print(f"브랜드 : {self.brand}")
        print(f"모델명 : {self.model}")
        print(f"색상 : {self.color}")
        print(f"현재속도 : {self.speed}")


# 객체 생성 및 사용
my_car = Car("tesla", 'model3', "빨간색")
my_car.info()
my_car.accelerate(80)
my_car.brake(30)
my_car.info()

# 실습1


class Book:
    def __init__(self, title, author, total_pages, current_page):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page

    def read_page(self, pages):
        self.current_page = min(self.total_pages, self.current_page+pages)

    def progress(self):
        pct = (self.current_page/self.total_pages)*100
        return round(pct, 1)

    def info(self):
        print(f"책이름 : {self.title}")
        print(f"저자 : {self.author}")
        print(f"전체 페이지수 : {self.total_pages}")
        print(f"현재 페이지수 : {self.current_page}")


my_book = Book("python", "홍길동", 320, 60)
my_book.read_page(100)
my_book.progress
print(my_book.info())

# width, height = input("두 숫자를 입력하세요 : ".split())


class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def area(self):
        area1 = self.width*self.height
        return area1


width, height = input("두 숫자를 입력하세요").split()
squ = Rectangle(width, height)
print(squ.area())
