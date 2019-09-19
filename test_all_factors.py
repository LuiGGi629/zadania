import unittest
from all_factors import get_all_factors


class GetAllFactorsTests(unittest.TestCase):
    """Tests for get_all_factors."""
    def test_small_numbers(self):
        inputs = {1, 2, 3, 4}
        outputs = {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4]}
        self.assertEqual(get_all_factors(inputs), outputs)

    def test_large_numbers(self):
        inputs = {62, 293, 314}
        outputs = {62: [1, 2, 31, 62], 293: [1, 293], 314: [1, 2, 157, 314]}
        self.assertEqual(get_all_factors(inputs), outputs)


if __name__ == '__main__':
    unittest.main(verbosity=2)
