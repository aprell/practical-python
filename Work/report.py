# Exercises 2.4-2.7
# Exercises 2.9-2.12
# Exercises 2.16, 2.20, 2.24, 2.25
# Exercises 3.1, 3.2, 3.12, 3.15, 3.16, 3.18
# Exercises 4.3-4.8
# Exercise 5.6
# Exercise 6.2
# Exercises 7.3, 7.4, 7.11
# Exercise 8.3

from fileparse import parse_csv
from portfolio import Portfolio
from tableformat import create_formatter
import sys

def read_prices(filename, **opts):
    with open(filename, "rt") as file:
        prices = parse_csv(
            file,
            has_headers=False,
            types=[str, float],
            **opts
        )
    return {
        name: price for name, price in prices
    }

def read_portfolio(filename, **opts):
    with open(filename, "rt") as file:
        return Portfolio.from_csv(file, **opts)

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
    import logging
    logging.basicConfig(level=logging.ERROR)
    main(sys.argv)
