# Exercises 4.1, 4.2, 4.9
# Exercises 5.6-5.8
# Exercises 7.7-7.9

from typedproperty import String, Integer, Float

class Stock:
    __slots__ = ("_name", "_shares", "_price")

    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price:.2f})"

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        shares = min(shares, self.shares)
        self.shares -= shares
