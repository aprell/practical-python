# Exercises 4.1, 4.2

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        shares = min(shares, self.shares)
        self.shares -= shares
