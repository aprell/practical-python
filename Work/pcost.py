# Exercises 1.27, 1.30-1.33
# Exercises 2.15, 2.16
# Exercise 3.14

from report import read_portfolio
import sys

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    portfolio_price = 0
    for holding in portfolio:
        portfolio_price += holding["shares"] * holding["price"]
    return portfolio_price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

print("\u2211", portfolio_cost(filename))
