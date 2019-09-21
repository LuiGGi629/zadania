from collections import namedtuple
import csv


def parse_csv(file):
    """Return namedtuple list representing data from given file object."""
    csv_reader = csv.reader(file)
    Row = namedtuple("Row", next(csv_reader))
    return [Row(*values) for values in csv_reader]
