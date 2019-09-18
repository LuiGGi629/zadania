import unittest
from dict_from_truple import dict_from_truple


class DictFromTupleTests(unittest.TestCase):
    """Tests for dict_from_truple."""
    def test_three_tuples(self):
        inputs = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        outputs = {1: (2, 3), 4: (5, 6), 7: (8, 9)}
        self.assertEqual(dict_from_truple(inputs), outputs)

    def test_four_items(self):
        inputs = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)]
        outputs = {1: (2, 3, 4), 5: (6, 7, 8), 9: (10, 11, 12)}
        self.assertEqual(dict_from_truple(inputs), outputs)


if __name__ == '__main__':
    unittest.main(verbosity=2)
