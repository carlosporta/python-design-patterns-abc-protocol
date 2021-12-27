# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Visitor.html

from abc import ABC, abstractmethod
from typing import Any


class IVisitor(ABC):
    @abstractmethod
    def visit(self, element: Any) -> None:
        ...


class IVisitable(ABC):
    @abstractmethod
    def accept(self, visitor: IVisitor) -> None:
        ...


class Flower(IVisitable):
    def accept(self, visitor: IVisitor) -> None:
        visitor.visit(self)

    def pollinate(self, pollinator: IVisitor) -> None:
        print(self, "pollinated by", pollinator)

    def eat(self, eater: IVisitor) -> None:
        print(self, "eaten by", eater)


class Bug(IVisitor):
    pass


class Pollinator(Bug):
    pass


class Predator(Bug):
    pass


class Bee(Pollinator):
    def visit(self, flower: Flower) -> None:
        flower.pollinate(self)


class Fly(Pollinator):
    def visit(self, flower: Flower) -> None:
        flower.pollinate(self)


class Worm(Predator):
    def visit(self, flower: Flower) -> None:
        flower.eat(self)


if __name__ == "__main__":
    bee = Bee()
    fly = Fly()
    worm = Worm()
    flower = Flower()
    flower.accept(bee)
    flower.accept(fly)
    flower.accept(worm)
