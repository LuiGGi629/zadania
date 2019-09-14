import unittest
from all_together import all_together


class AllTogetherTests(unittest.TestCase):
    """Tests for all_together."""
    def test_list_and_tuple(self):
        outputs = list(all_together([1, 2], (3, 4)))
        expected = [1, 2, 3, 4]
        self.assertEqual(outputs, expected)

    def test_with_strings(self):
        outputs = list(all_together([1, 2], (3, 4), "elo"))
        expected = [1, 2, 3, 4, "e", "l", "o"]
        self.assertEqual(outputs, expected)

    def test_empty_list(self):
        outputs = list(all_together([], (), "", [1, 2]))
        self.assertEqual(outputs, [1, 2])


if __name__ == '__main__':
    unittest.main(verbosity=2)
