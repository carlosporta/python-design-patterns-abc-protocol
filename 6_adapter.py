from abc import ABC, abstractmethod
from typing import Iterable


class IReportItem(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError


class ReportItem(IReportItem):
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name


class Report:
    def __init__(self, items: Iterable[IReportItem]) -> None:
        self.items = items

    def display(self) -> None:
        print("Items")
        for item in self.items:
            print(f"Name: {item.name}")


class Item:
    def __init__(self, title: str) -> None:
        self.title = title


class ReportItemAdapter(IReportItem):
    def __init__(self, item: Item) -> None:
        self.item = item

    @property
    def name(self) -> str:
        return self.item.title


if __name__ == "__main__":
    items = (
        ReportItemAdapter(Item("Foo")),
        ReportItemAdapter(Item("Bar")),
        ReportItemAdapter(Item("Foobar")),
    )
    report = Report(items)
    report.display()
