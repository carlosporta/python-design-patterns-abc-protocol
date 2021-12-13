from random import uniform
from typing import Protocol
from math import pi


class Shape(Protocol):
    def area(self) -> float:
        ...


class Circle:
    def __init__(self) -> None:
        self.radius = uniform(0, 1)

    def area(self) -> float:
        return self.radius * pi


class Rectangle:
    def __init__(self) -> None:
        self.width = uniform(0, 1)
        self.lenght = uniform(0, 1)

    def area(self) -> float:
        return self.width * self.lenght


class ShapeFactory:
    def create(self, shape_type: str) -> Shape:
        # error: Incompatible return value type (got "object", expected "Shape")
        # Issue created: https://github.com/python/mypy/issues/11722
        # return Circle() if shape_type == 'circle' else Rectangle()

        if shape_type == 'circle':
            return Circle()
        else:
            return Rectangle()


shape_factory = ShapeFactory()
shape_type = input('Type a shape name (rectangle (fallback) or circle): ')
shape = shape_factory.create(shape_type)
classname = type(shape).__name__
print(f'The area of this {classname} is {shape.area():.2f}')
