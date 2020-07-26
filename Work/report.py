# Exercises 2.4-2.7
# Exercises 2.9-2.12
# Exercises 2.16, 2.20, 2.24, 2.25
# Exercises 3.1, 3.2

from copy import deepcopy
import csv
import sys

def read_prices(filename):
    prices = {}
    with open(filename, "rt") as file:
        lines = csv.reader(file)
        for lineno, line in enumerate(lines, start=1):
            try:
                prices[line[0]] = float(line[1])
            except (IndexError, ValueError):
                print(f"Skipping {filename}, line {lineno}:", line, file=sys.stderr)
    return prices

def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as file:
        lines = csv.reader(file)
        keys = next(lines)
        # Keys of interest and the types of their values
        types = {"name": str, "shares": int, "price": float}
        for lineno, line in enumerate(lines, start=1):
            record = dict(zip(keys, line))
            try:
                portfolio.append({
                    name: cast(record[name]) for name, cast in types.items()
                })
            except ValueError:
                print(f"Skipping {filename}, line {lineno}:", line, file=sys.stderr)
    return portfolio

def portfolio_cost(portfolio, verbose=True):
    if verbose:
        portfolio_price = 0
        for holding in portfolio:
            name, shares, price = holding["name"], holding["shares"], holding["price"]
            purchase_price = shares * price
            print(f"{name:5}: {shares:3} x {price:6.2f} = {purchase_price:10,.2f}")
            portfolio_price += purchase_price
        return portfolio_price
    else:
        return sum([holding["shares"] * holding["price"] for holding in portfolio])

def portfolio_value(portfolio, prices, verbose=True):
    portfolio = deepcopy(portfolio)
    for holding in portfolio:
        holding["price"] = prices[holding["name"]]
    return portfolio_cost(portfolio, verbose)

def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        report.append(
            {
                "name": holding["name"],
                "shares": holding["shares"],
                "price": prices[holding["name"]],
                "change": prices[holding["name"]] - holding["price"]
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

if len(sys.argv) == 2:
    filename = sys.argv[1]
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
