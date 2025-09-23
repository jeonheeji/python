# 상속
# 기존 클래스의 속성과 메서드를 물려받아 새로운 클래스를 만드는것
# 동물 : 포유류 -> 개, 고양이 (공통 특징 : 털, 먹기)
# 자동차 : 차량 -> 승용차, 트럭
# 가족 : 부모 -> 자식

# 상속없이 -> 코드 중복 심각
# 너무 많은 중복 -> 상속으로 해결

class Animal:  # 부모
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name}가 잠을 잡니다")


class Dog(Animal):
    def bark(self):
        print(f"{self.name}가 멍멍 짖습니다")


dog1 = Dog("바둑이", 3)
dog1.bark()

# 기본 문법과 용어


class 부모클래스:
    # 부모 클래스 내용
    pass


class 자식클래스(부모클래스):
    # 자식 클래스 내용
    pass
# 자식은 부모의 모든 것을 물려받는다
# 부모의 모든 속성과 메서드를 자동으로 사용 가능
# 추가된 자신만의 속성과 메서드 정의도 가능


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"안녕하세요, {self.name} 입니다")


class Student(Person):
    def study(self):
        print(f"{self.name}가 공부합니다")


class Teacher(Person):
    def teach(self):
        print(f"{self.name}가 수업합니다")


student = Student("김학생", 20)
teacher = Teacher("박선생", 35)

student.greet()  # 부모 클래스 메서드 호출
teacher.greet()

student.study()  # 자식 클래스 메서드 호출
teacher.teach()

# super()와 생성자 상속
# super()
# 자식 클래스에서 부모 클래스에 접근할때 사용

# super() 없이 - 문제 발생!


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"person 생성 : {name}{age}살")


class Student(Person):
    def __init__(self, name, age, student_id):  # init은 덮어쓰기 가능 -> 그래서 name과 age가 정의되지 않은게 됨
        # 부모 클래스의 __init__ 을 호출하지 않음
        super().__init__(name, age)  # 부모클래스의 init을 그대로 쓴다!
        self.student_id = student_id
        print(f"student 생성 {self.student_id}")


student = Student("kim", 20, "1234")
print(student.name)

# 메서드 오버라이딩
# 오버라이딩
# 부모 클래서의 메서드를 자식 클래스에서 다시 정의 하는것


class Animal:
    def make_sound(self):
        print(f"소리를냄")


class Dog(Animal):
    def make_sound(self):
        print("멍멍")


class Cat(Animal):
    def make_sound(self):
        print("야옹")


animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def info(self):
        print(f"{self.name}의 넓이: {self.area()}")


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("직사각형")
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("원")
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius


shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    shape.info()
