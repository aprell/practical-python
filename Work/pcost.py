# Exercises 1.27, 1.30-1.33

import csv
import sys

def portfolio_cost(filename):
    portfolio_price = 0
    with open(filename, "rt") as file:
        lines = csv.reader(file)
        # Skip header
        next(lines)
        for line in lines:
            try:
                name = line[0]
                shares = int(line[1])
                price = float(line[2])
                purchase_price = shares * price
                print(f"{name:5}: {shares:3} x {price:5.2f} = {purchase_price:8.2f}")
                portfolio_price += purchase_price
            except ValueError:
                print("Warning: skipping", line, file=sys.stderr)
    return portfolio_price

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

print("\n\u2211", portfolio_cost(filename))
