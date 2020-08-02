# Exercises 4.5, 4.6

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