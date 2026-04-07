class Shape:
    def calculateArea():
        pass
    def calculatePerimeter():
        pass

class Square(Shape):
    def __int__(self, side):
        super().__init__()
        self.side = side

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius