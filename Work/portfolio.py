# Exercise 6.2

class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return iter(self._holdings)

    @property
    def total_cost(self):
        return sum([holding.cost for holding in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for holding in self._holdings:
            total_shares[holding.name] += holding.shares
        return total_shares
