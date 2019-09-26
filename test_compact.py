import unittest
from compact import compact


class CompactTests(unittest.TestCase):
    """Tests for compact."""
    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_no_duplicates(self):
        self.assertIterableEqual(compact([1, 2, 3]), [1, 2, 3])

    def test_adjacent_duplicates(self):
        self.assertIterableEqual(compact([1, 1, 2, 2, 3]), [1, 2, 3])

    def test_non_adjacent_duplicates(self):
        self.assertIterableEqual(compact([1, 2, 3, 1, 2]), [1, 2, 3, 1, 2])

    def test_lots_adjacent_duplicates(self):
        self.assertIterableEqual(compact([1, 1, 1, 1, 1, 1]), [1])

    def test_empty_values(self):
        self.assertIterableEqual(compact([None, 0, "", []]), [None, 0, "", []])

    def test_empty_list(self):
        self.assertIterableEqual(compact([]), [])

    def test_accepts_iterator(self):
        nums = (n**2 for n in [1, 2, 3])
        self.assertIterableEqual(compact(nums), [1, 4, 9])

    def test_returns_iterator(self):
        nums = iter([1, 2, 3])
        output = compact(nums)
        self.assertEqual(iter(output), iter(output))
        self.assertEqual(next(output), 1)
        self.assertEqual(next(nums), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
