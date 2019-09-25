import unittest
from coprime import coprime


class CoprimeTests(unittest.TestCase):
    """Tests for coprime."""
    def test_2_and_5(self):
        self.assertTrue(coprime(2, 5))

    def test_2_and_6(self):
        self.assertFalse(coprime(2, 6))

    def test_4_and_9(self):
        self.assertTrue(coprime(4, 9))

    def test_3_and_9(self):
        self.assertFalse(coprime(3, 9))


if __name__ == '__main__':
    unittest.main(verbosity=2)
