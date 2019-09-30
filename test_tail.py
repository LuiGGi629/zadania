import unittest
from tail import tail


class TailTests(unittest.TestCase):
    """Tests for tail."""
    def test_zero(self):
        self.assertEqual(tail([1, 2], 0), [])

    def test_one(self):
        self.assertEqual(tail([1, 2], 1), [2])

    def test_two(self):
        self.assertEqual(tail([1, 2], 2), [1, 2])

    def test_n_larger_than_iterable_length(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(tail(nums, 5), [1, 2, 3, 4])
        self.assertEqual(tail([], 10), [])

    def test_string(self):
        self.assertEqual(tail("elo", 2), ["l", "o"])

    def test_tuple(self):
        self.assertEqual(tail((1, 2, 3), 3), [1, 2, 3])


if __name__ == '__main__':
    unittest.main(verbosity=2)
