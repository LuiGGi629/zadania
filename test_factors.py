import unittest
from factors import get_factors


class GetFactorsTests(unittest.TestCase):
    """Tests for get_factors."""
    def test_2(self):
        self.assertEqual(get_factors(2), [1, 2])

    def test_6(self):
        self.assertEqual(get_factors(6), [1, 2, 3, 6])

    def test_100(self):
        self.assertEqual(get_factors(100), [1, 2, 4, 5, 10, 20, 25, 50, 100])


if __name__ == '__main__':
    unittest.main(verbosity=2)
