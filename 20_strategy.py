from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    abstractmethod
    def calculate_tax_price(self, price: float) -> float:
        raise NotImplementedError


class OldTaxCalculator(TaxCalculator):
    def calculate_tax_price(self, price: float) -> float:
        return .01 * price


class NewTaxCalculator(TaxCalculator):
    def calculate_tax_price(self, price: float) -> float:
        return .02 * price + 2


class Invoice:
    def __init__(self, price: float, tax_calculator: TaxCalculator) -> None:
        self.price = price
        self.tax_calculator = tax_calculator

    @property
    def tax_price(self) -> float:
        return self.tax_calculator.calculate_tax_price(self.price)

    @property
    def price_plus_tax(self) -> float:
        return self.tax_price + self.price


if __name__ == "__main__":
    invoice = Invoice(10, OldTaxCalculator())
    print("Old calculator")
    print(f"Invoice price: {invoice.price}")
    print(f"Invoice tax price: {invoice.tax_price}")
    print(f"Invoice price plus tax: {invoice.price_plus_tax}")

    print()
    invoice.tax_calculator = NewTaxCalculator()
    print("New calculator")
    print(f"Invoice price: {invoice.price}")
    print(f"Invoice tax price: {invoice.tax_price}")
    print(f"Invoice price plus tax: {invoice.price_plus_tax}")