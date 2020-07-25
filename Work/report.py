# Exercises 2.4-2.7
# Exercises 2.9-2.12

from copy import deepcopy
import csv
import sys

def read_prices(filename):
    prices = {}
    with open(filename, "rt") as file:
        lines = csv.reader(file)
        for line in lines:
            try:
                prices[line[0]] = float(line[1])
            except (IndexError, ValueError):
                print("Warning: skipping", line, file=sys.stderr)
    return prices

def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as file:
        lines = csv.reader(file)
        # Skip header
        next(lines)
        for line in lines:
            try:
                portfolio.append(
                    {
                        "name": line[0],
                        "shares": int(line[1]),
                        "price": float(line[2])
                    }
                )
            except ValueError:
                print("Warning: skipping", line, file=sys.stderr)
    return portfolio

def portfolio_cost(portfolio):
    portfolio_price = 0
    for holding in portfolio:
        name, shares, price = holding["name"], holding["shares"], holding["price"]
        purchase_price = shares * price
        print(f"{name:5}: {shares:3} x {price:6.2f} = {purchase_price:10,.2f}")
        portfolio_price += purchase_price
    return portfolio_price

def portfolio_value(portfolio, prices):
    portfolio = deepcopy(portfolio)
    for holding in portfolio:
        holding["price"] = prices[holding["name"]]
    return portfolio_cost(portfolio)

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
    hlines = (10 * "-", 10 * "-", 10 * "-", 10 * "-")
    print("%10s %10s %10s %10s" % headers)
    print(" ".join(hlines))
    for line in make_report(portfolio, prices):
        line["price"] = "$%.2f" % line["price"]
        print("{name:>10s} {shares:>10d} {price:>10s} {change:>+10.2f}".format_map(line))

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

portfolio = read_portfolio(filename)
#cost = portfolio_cost(portfolio)
#print(f"\n\u2211 {cost:,.2f}\n")

prices = read_prices("Data/prices.csv")
#value = portfolio_value(portfolio, prices)
#print(f"\n\u2211 {value:,.2f}\n")

#print(f"{value:,.2f} - {cost:,.2f} = {value - cost:,.2f}")

print_report(portfolio, prices)
