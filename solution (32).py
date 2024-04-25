class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

class CalculatePerimeterMixin(Rectangle):
    def calculate_perimeter(self):
        return 2 * (self.a + self.b)

class SquareWithMixin(CalculatePerimeterMixin, Square):
    def __eq__(self, other):
        return self.a == other.a

    def __gt__(self, other):
        return self.calculate_area() > other.calculate_area()

    def __add__(self, other):
        return self.calculate_area() + other.calculate_area()

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)