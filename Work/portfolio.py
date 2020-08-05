# Exercises 6.2, 6.3, 6.14

class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return iter(self._holdings)

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(name == holding.name for holding in self._holdings)

    @property
    def total_cost(self):
        return sum(holding.cost for holding in self._holdings)

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for holding in self._holdings:
            total_shares[holding.name] += holding.shares
        return total_shares
