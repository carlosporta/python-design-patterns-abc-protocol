from random import uniform
from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError

class Circle(Shape):
    def __init__(self) -> None:
        self.radius = uniform(0, 1)

    def area(self) -> float:
        return self.radius * pi


class Rectangle(Shape):
    def __init__(self) -> None:
        self.width = uniform(0, 1)
        self.lenght = uniform(0, 1)

    def area(self) -> float:
        return self.width * self.lenght


class ShapeFactory:
    def create(self, shape_type: str) -> Shape:
        return Circle() if shape_type == 'circle' else Rectangle()


shape_factory = ShapeFactory()
shape_type = input('Type a shape name (rectangle (fallback) or circle): ')
shape = shape_factory.create(shape_type)
classname = type(shape).__name__
print(f'The area of this {classname} is {shape.area():.2f}')
