# Exercises 2.4-2.7
# Exercises 2.9-2.12
# Exercises 2.16, 2.20, 2.24, 2.25
# Exercises 3.1, 3.2, 3.12, 3.15, 3.16, 3.18
# Exercises 4.3-4.8
# Exercise 5.6
# Exercise 6.2
# Exercise 7.3

from fileparse import parse_csv
from portfolio import Portfolio
from stock import Stock
from tableformat import create_formatter
import sys

def read_prices(filename):
    with open(filename, "rt") as file:
        prices = parse_csv(
            file,
            has_headers=False,
            types=[str, float]
        )
    return {
        name: price for name, price in prices
    }

def read_portfolio(filename):
    with open(filename, "rt") as file:
        portfolio = parse_csv(
            file,
            has_headers=True,
            select=["name", "shares", "price"],
            types={"shares": int, "price": float}
        )
    return Portfolio([
        Stock(**holding) for holding in portfolio
    ])

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        report.append(
            {
                "name": holding.name,
                "shares": holding.shares,
                "price": prices[holding.name],
                "change": prices[holding.name] - holding.price
            }
        )
    return report

def print_report(portfolio, prices, formatter):
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for line in make_report(portfolio, prices):
        formatter.row([
            line["name"],
            str(line["shares"]),
            "$%.2f" % line["price"],
            "%.2f" % line["change"]
        ])

def portfolio_report(portfolio_filename, prices_filename, fmt="txt"):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    print_report(portfolio, prices, create_formatter(fmt)())

def main(argv):
    assert len(argv) >= 2
    filename = argv[1]
    if len(argv) > 2:
        fmt = argv[2]
    else:
        fmt = "txt"

    portfolio_report(filename, "Data/prices.csv", fmt)

if __name__ == "__main__":
    main(sys.argv)
