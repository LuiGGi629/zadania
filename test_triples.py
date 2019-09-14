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

    def test_triples_100(self):
        expected = [(3, 4, 5),
                    (5, 12, 13),
                    (6, 8, 10),
                    (7, 24, 25),
                    (8, 15, 17),
                    (9, 12, 15),
                    (9, 40, 41),
                    (10, 24, 26),
                    (11, 60, 61),
                    (12, 16, 20),
                    (12, 35, 37),
                    (13, 84, 85),
                    (14, 48, 50),
                    (15, 20, 25),
                    (15, 36, 39),
                    (16, 30, 34),
                    (16, 63, 65),
                    (18, 24, 30),
                    (18, 80, 82),
                    (20, 21, 29),
                    (20, 48, 52),
                    (21, 28, 35),
                    (21, 72, 75),
                    (24, 32, 40),
                    (24, 45, 51),
                    (24, 70, 74),
                    (25, 60, 65),
                    (27, 36, 45),
                    (28, 45, 53),
                    (30, 40, 50),
                    (30, 72, 78),
                    (32, 60, 68),
                    (33, 44, 55),
                    (33, 56, 65),
                    (35, 84, 91),
                    (36, 48, 60),
                    (36, 77, 85),
                    (39, 52, 65),
                    (39, 80, 89),
                    (40, 42, 58),
                    (40, 75, 85),
                    (42, 56, 70),
                    (45, 60, 75),
                    (48, 55, 73),
                    (48, 64, 80),
                    (51, 68, 85),
                    (54, 72, 90),
                    (57, 76, 95),
                    (60, 63, 87),
                    (65, 72, 97)]
        self.assertEqual(triples(100), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
