import unittest
from transpose import transpose


class TransposeTests(unittest.TestCase):
    """Tests for transpose."""
    def test_empty(self):
        self.assertEqual(transpose([]), [])

    def test_single_item(self):
        self.assertEqual(transpose([[1]]), [[1]])

    def test_two_rows(self):
        self.assertEqual(transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_three_rows(self):
        inputs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        outputs = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(transpose(inputs), outputs)


if __name__ == '__main__':
    unittest.main(verbosity=2)
