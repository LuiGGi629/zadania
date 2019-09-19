import unittest
from matrix_from_string import matrix_from_string


class MatrixFromStringTests(unittest.TestCase):
    """Tests for matrix_from_string."""
    def test_two_by_two_matrix(self):
        matrix = matrix_from_string("1 2\n10 20")
        self.assertEqual([[1, 2], [10, 20]], matrix)

    def test_three_by_two_matrix(self):
        matrix = matrix_from_string("9 8 7\n19 18 17")
        self.assertEqual([[9, 8, 7], [19, 18, 17]], matrix)


if __name__ == '__main__':
    unittest.main(verbosity=2)
