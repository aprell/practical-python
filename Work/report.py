# Exercises 2.4-2.7
# Exercises 2.9-2.12
# Exercises 2.16, 2.20, 2.24, 2.25
# Exercises 3.1, 3.2, 3.12, 3.15, 3.16, 3.18
# Exercises 4.3, 4.4

from copy import deepcopy
from fileparse import parse_csv
from stock import Stock
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
    return [
        Stock(holding["name"], holding["shares"], holding["price"]) for holding in portfolio
    ]

def portfolio_cost(portfolio, verbose=True):
    if verbose:
        portfolio_price = 0
        for holding in portfolio:
            purchase_price = holding.cost()
            print(f"{holding.name:5}: {holding.shares:3} x {holding.price:6.2f} = {purchase_price:10,.2f}")
            portfolio_price += purchase_price
        return portfolio_price
    else:
        return sum([holding.cost() for holding in portfolio])

def portfolio_value(portfolio, prices, verbose=True):
    portfolio = deepcopy(portfolio)
    for holding in portfolio:
        holding.price = prices[holding.name]
    return portfolio_cost(portfolio, verbose)

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

def print_report(portfolio, prices):
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    print(" ".join((10 * "-",) * len(headers)))
    for line in make_report(portfolio, prices):
        line["price"] = "$%.2f" % line["price"]
        print("{name:>10s} {shares:>10d} {price:>10s} {change:>+10.2f}".format_map(line))

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    print_report(portfolio, prices)

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "Data/portfolio.csv"

    #portfolio = read_portfolio(filename)
    #cost = portfolio_cost(portfolio, verbose=False)
    #print(f"\n\u2211 {cost:,.2f}\n")

    #prices = read_prices("Data/prices.csv")
    #value = portfolio_value(portfolio, prices, verbose=False)
    #print(f"\n\u2211 {value:,.2f}\n")

    #print(f"{value:,.2f} - {cost:,.2f} = {value - cost:,.2f}")

    portfolio_report(filename, "Data/prices.csv")

if __name__ == "__main__":
    main(sys.argv)
