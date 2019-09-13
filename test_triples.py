import unittest
from triples import triples


class TriplesTests(unittest.TestCase):
    """Tests for triples."""
    def test_triples_1(self):
        expected = []
        self.assertEqual(triples(1), expected)

    def test_triples_6(self):
        expected = [(3, 4, 5)]
        self.assertEqual(triples(6), expected)

    def test_triples_25(self):
        expected = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17),
                    (9, 12, 15), (12, 16, 20)]
        self.assertEqual(triples(25), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
