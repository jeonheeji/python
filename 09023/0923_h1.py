class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printInfo(self):
        print(f"변의개수 : {self.sides}")
        print(f"밑변의 길이 : {self.base}")

    def area(self):
        print("넓이가 정의되지 않았습니다")


class Rectangle(Shape):
    def __init__(self, base, height):
        super().__init__("4", base)
        self.base = base
        self.height = height

    def area(self):
        print(f"넓이: {self.base*self.height}")


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("3", base)
        self.base = base
        self.height = height

    def area(self):
        print(f"넓이 :{self.base*self.height/2}")


shape1 = Rectangle(2, 3)
shape2 = Triangle(2, 4)

shape1.printInfo()
shape1.area()
shape2.printInfo()
shape2.area()
