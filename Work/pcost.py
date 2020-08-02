# Exercises 1.27, 1.30-1.33
# Exercises 2.15, 2.16
# Exercises 3.14-3.16
# Exercises 4.3, 4.4

from report import read_portfolio
import sys

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    portfolio_price = 0
    for holding in portfolio:
        portfolio_price += holding.cost()
    return portfolio_price

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "Data/portfolio.csv"

    print("\u2211", portfolio_cost(filename))

if __name__ == "__main__":
    main(sys.argv)