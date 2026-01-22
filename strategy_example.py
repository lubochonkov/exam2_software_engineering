from typing import Protocol


class DiscountStrategy(Protocol):
    def apply(self, price: float) -> float:
        ...


class NoDiscount:
    def apply(self, price: float) -> float:
        return price


class PercentageDiscount:
    def __init__(self, percent: float):
        self.percent = percent

    def apply(self, price: float) -> float:
        return price * (1 - self.percent / 100)


class Checkout:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def total(self, price: float) -> float:
        return self.strategy.apply(price)


if __name__ == "__main__":
    checkout = Checkout(NoDiscount())
    print("No discount:", checkout.total(100))

    checkout.set_strategy(PercentageDiscount(20))
    print("20% discount:", checkout.total(100))
    