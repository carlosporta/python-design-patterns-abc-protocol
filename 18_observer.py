from abc import ABC, abstractmethod
from typing import Any, Callable


OnEventCallback = Callable[[str, int, int], Any]


class Observer(ABC):
    def __init__(self, callback: OnEventCallback) -> None:
        self.callback = callback

    @abstractmethod
    def update(self, event: str, old: int, new: int) -> None:
        raise NotImplementedError


class OnIncreaseObserver(Observer):
    def __init__(self, callback: OnEventCallback) -> None:
        super().__init__(callback)

    def update(self, event: str, old: int, new: int) -> None:
        if event == "increase":
            self.callback(event, old, new)


class OnDecreaseObserver(Observer):
    def __init__(self, callback: OnEventCallback) -> None:
        super().__init__(callback)

    def update(self, event: str, old: int, new: int) -> None:
        if event == "decrease":
            self.callback(event, old, new)


class OnChangeObserver(Observer):
    def __init__(self, callback: OnEventCallback) -> None:
        super().__init__(callback)

    def update(self, event: str, old: int, new: int) -> None:
        self.callback(event, old, new)
            

class Value:
    def __init__(self, value: int) -> None:
        self._value = value
        self.observers: list[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def decrease(self) -> int:
        return self._update_value(-1, "decrease")

    def increase(self) -> int:
        return self._update_value(1, "increase")

    def _update_value(self, amount: int, event: str) -> int:
        old = self._value
        new = self._value + amount
        self._value = new
        self.notify(event, old, new)
        return self._value

    def notify(self, event: str, old: int, new: int) -> None:
        for observer in self.observers:
            observer.update(event, old, new)


def on_value_increased(old: int, new: int) -> None:
    print(f"Value increased from {old} to {new}")

def on_value_decreased(old: int, new: int) -> None:
    print(f"Value decreased from {old} to {new}")

def on_value_changed(event: str, old: int, new: int) -> None:
    print(f"Event: {event} from {old} to {new}")

if __name__ == "__main__":
    value = Value(10)
    value.add_observer(OnIncreaseObserver(lambda _, old, new: on_value_increased(old, new)))
    value.add_observer(OnDecreaseObserver(lambda _, old, new: on_value_decreased(old, new)))
    value.add_observer(OnChangeObserver(on_value_changed))

    value.increase()
    value.decrease()