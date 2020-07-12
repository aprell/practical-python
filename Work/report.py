# Exercises 2.4, 2.5

import csv
import sys

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

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    portfolio_price = 0
    for holding in portfolio:
        name, shares, price = holding["name"], holding["shares"], holding["price"]
        purchase_price = shares * price
        print(f"{name:5}: {shares:3} x {price:5.2f} = {purchase_price:8.2f}")
        portfolio_price += purchase_price
    return portfolio_price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

print("\n\u2211", portfolio_cost(filename))
