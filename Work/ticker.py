# Exercises 6.10-6.12

import csv
from follow import follow

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [convert(val) for convert, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_names(rows, names):
    for row in rows:
        if row["name"] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows

def ticker(filename, logfilename, fmt):
    from report import read_portfolio
    from tableformat import create_formatter

    portfolio = read_portfolio(filename)
    lines = follow(logfilename)
    rows = parse_stock_data(lines)
    rows = filter_names(rows, portfolio)
    formatter = create_formatter(fmt)()

    formatter.headings(["Name", "Price", "Change"])

    for row in rows:
        formatter.row([
            row["name"],
            "$%.2f" % row["price"],
            "%.2f" % row["change"]
        ])

if __name__ == "__main__":
    ticker("Data/portfolio.csv", "Data/stocklog.csv", "txt")
