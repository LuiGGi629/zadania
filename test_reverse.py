import unittest
from reverse import reverse_difference


class ReverseDifferenceTests(unittest.TestCase):
    """Tests for reverse_difference."""
    def test_empty(self):
        self.assertEqual(reverse_difference([]), [])

    def test_one(self):
        self.assertEqual(reverse_difference([1]), [0])

    def test_two(self):
        self.assertEqual(reverse_difference([0, 0]), [0, 0])

    def test_three(self):
        self.assertEqual(reverse_difference([3, 2, 1]), [2, 0, -2])

    def test_four(self):
        self.assertEqual(reverse_difference([9, 8, 7, 6]), [3, 1, -1, -3])

    def test_five(self):
        inputs = [1, 2, 3, 4, 5]
        outputs = [-4, -2, 0, 2, 4]
        self.assertEqual(reverse_difference(inputs), outputs)


if __name__ == '__main__':
    unittest.main(verbosity=2)
