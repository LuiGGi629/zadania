import unittest
from parse_ranges import parse_ranges


class ParseRangesTests(unittest.TestCase):
    """Tests for parse_ranges."""

    def test_single_range(self):
        self.assertEqual(list(parse_ranges("1-4")), [1, 2, 3, 4])

    def test_three_ranges(self):
        self.assertEqual(list(parse_ranges("1-2,4-4,8-10")),
                         [1, 2, 4, 8, 9, 10])

    def test_four_ranges(self):
        self.assertEqual(list(parse_ranges("6-9,0-0,20-23,66-69")),
                         [6, 7, 8, 9, 0, 20, 21, 22, 23, 66, 67, 68, 69])

    def test_is_iterator(self):
        self.assertEqual(next(parse_ranges("1-4")), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
