from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


@dataclass
class Burguer:
    name: str
    lettuce_grams: float
    tomato_grams: float
    bacon_grams: float
    cheese_grams: float

    def __init__(
        self,
        name: str,
        lettuce_grams: float,
        tomato_grams: float,
        bacon_grams: float,
        cheese_grams: float,
    ) -> None:
        self.name = name
        self.lettuce_grams = lettuce_grams
        self.tomato_grams = tomato_grams
        self.bacon_grams = bacon_grams
        self.cheese_grams = cheese_grams


class GramQuantity(Enum):
    LITTLE = 1.0
    NORMAL = 2.0
    ALOT = 3.0


class BurgerBuilder(ABC):
    @abstractmethod
    def build_name(self, name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def build_lettuce_grams(self, grams: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def build_tomato_grams(self, grams: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def build_bacon_grams(self, grams: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def build_cheese_grams(self, grams: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def build(self) -> Burguer:
        raise NotImplementedError


class CheeseBaconBuilder(BurgerBuilder):
    def __init__(self) -> None:
        self._reset()

    def _reset(self) -> None:
        self.burger = Burguer("", 0, 0, 0, 0)

    def build_name(self, name: str) -> None:
        self.burger.name = name

    def build_lettuce_grams(self, grams: float) -> None:
        self.burger.lettuce_grams = grams

    def build_tomato_grams(self, grams: float) -> None:
        self.burger.tomato_grams = grams

    def build_bacon_grams(self, grams: float) -> None:
        self.burger.bacon_grams = grams

    def build_cheese_grams(self, grams: float) -> None:
        self.burger.cheese_grams = grams

    def build(self) -> Burguer:
        self.build_name("Cheese Bacon")
        self.build_lettuce_grams(GramQuantity.LITTLE.value)
        self.build_tomato_grams(GramQuantity.LITTLE.value)
        self.build_bacon_grams(GramQuantity.ALOT.value)
        self.build_cheese_grams(GramQuantity.NORMAL.value)
        return self.burger


class CheeseSaladBuilder(BurgerBuilder):
    def __init__(self) -> None:
        self._reset()

    def _reset(self) -> None:
        self.burger = Burguer("", 0, 0, 0, 0)

    def build_name(self, name: str) -> None:
        self.burger.name = name

    def build_lettuce_grams(self, grams: float) -> None:
        self.burger.lettuce_grams = grams

    def build_tomato_grams(self, grams: float) -> None:
        self.burger.tomato_grams = grams

    def build_bacon_grams(self, grams: float) -> None:
        self.burger.bacon_grams = grams

    def build_cheese_grams(self, grams: float) -> None:
        self.burger.cheese_grams = grams

    def build(self) -> Burguer:
        self.build_name("Cheese Salad")
        self.build_lettuce_grams(GramQuantity.ALOT.value)
        self.build_tomato_grams(GramQuantity.ALOT.value)
        self.build_bacon_grams(GramQuantity.LITTLE.value)
        self.build_cheese_grams(GramQuantity.NORMAL.value)
        return self.burger


class Director:
    def set_builder(self, builder: BurgerBuilder) -> None:
        self.builder = builder

    def get_burger(self) -> Burguer:
        return self.builder.build()


cheese_bacon_builder = CheeseBaconBuilder()
cheese_salad_builder = CheeseSaladBuilder()
director = Director()

director.set_builder(cheese_bacon_builder)
print(director.get_burger())

director.set_builder(cheese_salad_builder)
print(director.get_burger())
