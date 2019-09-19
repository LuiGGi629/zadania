import unittest
from multi_valued_dict import multi_valued_dict


class MultiValuedDictTests(unittest.TestCase):
    """Tests for multi_valued_dict function."""
    def test_four_items(self):
        inputs = [(1, 2, 3, 4), (5, 6, 7, 8)]
        outputs = {1: (2, 3, 4), 5: (6, 7, 8)}
        self.assertEqual(multi_valued_dict(inputs), outputs)

    def test_three_items(self):
        inputs = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        outputs = {1: (2, 3), 4: (5, 6), 7: (8, 9)}
        self.assertEqual(multi_valued_dict(inputs), outputs)


if __name__ == '__main__':
    unittest.main(verbosity=2)
