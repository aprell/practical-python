# Exercises 4.1, 4.2, 4.9
# Exercise 5.6

class Stock:
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
