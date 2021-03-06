# Exercises 3.3-3.10, 3.17
# Exercise 8.2

import csv
import logging

log = logging.getLogger(__name__)

def parse_csv_dicts(lines, delimiter, select=None, types=None):
    """
    Parse lines in CSV format into a list of dicts
    """
    records = []
    lines = csv.reader(lines, delimiter=delimiter)
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

    for lineno, line in enumerate(lines, start=1):
        try:
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
        except ValueError as err:
            log.warning("Skipping line %d: %s", lineno, line)
            log.debug("Reason: %s", err)

    return records

def parse_csv_tuples(lines, delimiter, types=None):
    """
    Parse lines in CSV format into a list of tuples
    """
    records = []
    lines = csv.reader(lines, delimiter=delimiter)

    for lineno, line in enumerate(lines, start=1):
        try:
            if not line:
                continue
            if types:
                assert len(types) == len(line)
                line = [convert(val) for convert, val in zip(types, line)]
            records.append(tuple(line))
        except ValueError as err:
            log.warning("Skipping line %d: %s", lineno, line)
            log.debug("Reason: %s", err)

    return records

# The revenge for straying off course...
def parse_csv(lines, has_headers, delimiter=',', select=None, types=None):
    assert type(lines) is not str
    if has_headers:
        if types:
            assert type(types) is dict
        return parse_csv_dicts(lines, delimiter, select, types)
    else:
        if select:
            raise RuntimeError("select requires column names")
        if types:
            assert type(types) is list
        return parse_csv_tuples(lines, delimiter, types)
