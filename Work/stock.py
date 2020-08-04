# Exercises 4.1, 4.2, 4.9
# Exercises 5.6-5.8

class Stock:
    __slots__ = ("name", "_shares", "price")

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name}, {self.shares}, {self.price:.2f})"

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, shares):
        if type(shares) is not int:
            raise TypeError("Expected int")
        self._shares = shares

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        shares = min(shares, self.shares)
        self.shares -= shares
