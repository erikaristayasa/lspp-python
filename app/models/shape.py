import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculateArea(self) -> float:
        pass

    @abstractmethod
    def calculatePerimeter(self) -> float:
        pass

class Square(Shape):
    def __init__(self, side:int):
        super().__init__()
        self.side = side

    def calculateArea(self) -> float:
        return self.side * self.side

    def calculatePerimeter(self) -> float:
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, length:int, width:int):
        super().__init__()
        self.length = length
        self.width = width

    def calculateArea(self) -> float:
        return self.length * self.width

    def calculatePerimeter(self) -> float:
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius:int):
        super().__init__()
        self.radius = radius

    def calculateArea(self) -> float:
        return math.pi * self.radius * self.radius

    def calculatePerimeter(self) -> float:
        return 2 * math.pi * self.radius