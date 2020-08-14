# Exercises 6.2, 6.3, 6.14
# Exercise 7.11
# Exercise 9.1

from .fileparse import parse_csv
from .stock import Stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    def __iter__(self):
        return iter(self._holdings)

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(name == holding.name for holding in self._holdings)

    def append(self, holding):
        if not isinstance(holding, Stock):
            raise TypeError("Expected a Stock instance")
        self._holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()

        portfolio = parse_csv(
            lines,
            has_headers=True,
            select=["name", "shares", "price"],
            types={"shares": int, "price": float},
            **opts
        )

        for holding in portfolio:
            self.append(Stock(**holding))

        return self

    @property
    def total_cost(self):
        return sum(holding.cost for holding in self._holdings)

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for holding in self._holdings:
            total_shares[holding.name] += holding.shares
        return total_shares
