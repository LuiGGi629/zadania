import unittest
from first_prime_over import first_prime_over


class FirstPrimeOverTests(unittest.TestCase):
    """Tests for first_prime_over."""
    def test_first_prime_over_one_million(self):
        self.assertEqual(first_prime_over(1000000), 1000003)

    def test_first_prime_over_three_million(self):
        self.assertEqual(first_prime_over(3000000), 3000017)


if __name__ == '__main__':
    unittest.main(verbosity=2)
