# 추상 클래스
# 직접 객체를 만들 수 없고, 반드시 상속 받아서 완성해야 사용할 수 있는 미완성 설계도

# 추상 클래스 없이
from abc import ABC, abstractmethod


class Animal:
    def make_sound(self):
        pass  # empty


class Dog(Animal):
    def eat(self):
        print("밥을 먹습니다")


dog = Dog()
dog.make_sound()  # 아무것도 일어나지 않음 -> 버그

# 그래서 추상클래스 사용


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        pass

    def eat(self):
        print("강아지가 밥을 먹습니다")


dog = Dog()


# 기본사용법

class 추상클래스이름(ABC):  # ABC 상속이 필수
    @abstractmethod
    def 추상메서드(self):
        pass

# 추상 메서드는 자식 클래스에서 반드시 구현해야함


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        pass

    def eat(self):
        print("강아지가 밥을 먹습니다")


# animal = Animal() -> 추상클래스 직접 생성 불가

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius


# shape = Shape() -> 불가능
circle = Circle(5)
print(circle.area())
