import unittest
import os
from parse_csv import parse_csv
from textwrap import dedent
from tempfile import NamedTemporaryFile, mkdtemp
from contextlib import contextmanager


@contextmanager
def make_file(contents=None):
    with NamedTemporaryFile(mode="wt", delete=False) as file:
        if contents:
            file.write(contents)
    try:
        yield file.name
    finally:
        os.remove(file.name)


class ParseCSVTests(unittest.TestCase):
    """Tests for parse_csv."""
    def test_sample_file(self):
        csv_data = dedent("""
            col1,col2,more_data
            1,2,3
            "a,b","c\td","e f"
        """).lstrip()
        with make_file(csv_data) as filename:
            with open(filename) as csv_file:
                csv_rows = list(parse_csv(csv_file))
        self.assertEqual(len(csv_rows), 2)
        row1, row2 = csv_rows
        self.assertEqual(row1.col1, "1")
        self.assertEqual(row1.col2, "2")
        self.assertEqual(row1.more_data, "3")
        self.assertEqual(row1, "1", "2", "3")
        self.assertEqual(row2, "a,b", "c\td", "e f")

    def test_state_capitals(self):
        with open("data/us-state-capitals.csv") as capitals_file:
            csv_rows = list(parse_csv(capitals_file))
        self.assertEqual(len(csv_rows), 50)
        self.assertEqual(csv_rows[0].state, "Alabama")
        self.assertEqual(csv_rows[0].capital, "Montgomery")
        self.assertEqual(csv_rows[0], ("Alabama", "Montgomery"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
