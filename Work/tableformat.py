# Exercises 4.5-4.7, 4.10

# Abstract base class
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, data):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join([f"{header:>10s}" for header in headers]))
        print(" ".join((10 * "-",) * len(headers)))

    def row(self, data):
        print(" ".join([f"{field:>10s}" for field in data]))

class CSVTableFormatter(TableFormatter):
    def __init__(self, delimiter=','):
        super().__init__()
        self.delimiter = delimiter

    def headings(self, headers):
        print(self.delimiter.join(headers))

    def row(self, data):
        print(self.delimiter.join(data))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>" + "".join([f"<th>{header}</th>" for header in headers]) + "</tr>")

    def row(self, data):
        print("<tr>" + "".join([f"<td>{field}</td>" for field in data]) + "</tr>")

def create_formatter(fmt):
    if fmt == "txt":
        return TextTableFormatter
    elif fmt == "csv":
        return CSVTableFormatter
    elif fmt == "html":
        return HTMLTableFormatter
    else:
        raise RuntimeError("Unknown format " + fmt)

def print_table(table, columns, formatter):
    formatter.headings(columns)
    table = [[str(getattr(row, column)) for column in columns] for row in table]
    for row in table:
        formatter.row(row)
