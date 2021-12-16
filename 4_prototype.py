from abc import ABC, abstractmethod
from copy import deepcopy
from typing import TypeVar


class Cloneable(ABC):
    def clone(self) -> 'Cloneable':
        return deepcopy(self)


class Shape(Cloneable):
    def __init__(self, shape_type: str) -> None:
        self.shape_type = shape_type

    @abstractmethod
    def render(self) -> str:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__("Circle")
        self.radius = radius

    def render(self) -> str:
        return f"Rendering a Circle of radius {self.radius}"


class Rectangle(Shape):
    def __init__(self, width: float, lenght: float) -> None:
        super().__init__("Rectangle")
        self.width = width
        self.lenght = lenght

    def render(self) -> str:
        return f"Rendering a Rectangle of width {self.width} and lenght {self.lenght}"
        

class ShapeCache:
    def __init__(self) -> None:
        self._items: dict[str, Shape] = {}

    def add(self, key: str, valeu: Shape) -> None:
        self._items[key] = valeu

    def get(self, key: str) -> Shape:
        return deepcopy(self._items[key])


if __name__ == "__main__":
    cache = ShapeCache()
    cache.add("circle", Circle(1))
    cache.add("rectangle", Rectangle(1, 2))

    circle = cache.get("circle")
    rect = cache.get("rectangle")
    print(circle.shape_type)
    print(circle.render())
    print(rect.shape_type)
    print(rect.render())
