import unittest
from flatten import flatten


class FlattenTests(unittest.TestCase):
    """Tests for flatten."""
    def test_3_by_4_matrix(self):
        matrix = [[row * 3 + incr for incr in range(1, 4)] for row in range(4)]
        flattenend = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(flatten(matrix), flattenend)


if __name__ == '__main__':
    unittest.main()
