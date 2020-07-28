# Exercises 3.3-3.7

import csv

def parse_csv_dicts(filename, delimiter, select=None, types=None):
    """
    Parse a CSV file into a list of dicts
    """
    records = []
    with open(filename, "rt") as file:
        lines = csv.reader(file, delimiter=delimiter)
        keys = next(lines)

        if select:
            columns = [keys.index(col) for col in select]
            keys = select
        else:
            columns = None

        if types:
            # Make sure that every column to select has a type or defaults to str
            for key in keys:
                if key not in types:
                    types[key] = str

        for line in lines:
            if not line:
                continue
            if columns:
                line = [line[i] for i in columns]
            if types:
                records.append({
                    key: types[key](line[i]) for i, key in enumerate(keys)
                })
            else:
                records.append(dict(zip(keys, line)))
    return records

def parse_csv_tuples(filename, delimiter, types=None):
    """
    Parse a CSV file into a list of tuples
    """
    records = []
    with open(filename, "rt") as file:
        lines = csv.reader(file, delimiter=delimiter)

        for line in lines:
            if not line:
                continue
            if types:
                assert len(types) == len(line)
                line = [convert(val) for convert, val in zip(types, line)]
            records.append(tuple(line))
    return records

# The revenge for straying off course...
def parse_csv(filename, has_headers, delimiter=',', select=None, types=None):
    if has_headers:
        if types:
            assert type(types) is dict
        return parse_csv_dicts(filename, delimiter, select, types)
    else:
        assert not select, "select not supported"
        if types:
            assert type(types) is list
        return parse_csv_tuples(filename, delimiter, types)
