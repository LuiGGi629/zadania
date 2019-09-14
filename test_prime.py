import unittest
from prime import is_prime


class PrimalityTests(unittest.TestCase):
    """Tests for is_prime."""
    def test_21(self):
        self.assertFalse(is_prime(21))

    def test_23(self):
        self.assertTrue(is_prime(23))


if __name__ == '__main__':
    unittest.main(verbosity=2)
