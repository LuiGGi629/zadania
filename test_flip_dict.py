import unittest
from flip_dict import flip_dict


class FlipDictTests(unittest.TestCase):
    """Tests for flip_dict functino."""
    def test_no_collisions(self):
        inputs = {
            "Python": "1998-06-09",
            "Java": "2000-06-09",
            "C#": "2002-06-09",
        }
        outputs = {
            "2002-06-09": "C#",
            "2000-06-09": "Java",
            "1998-06-09": "Python",
        }
        self.assertEqual(flip_dict(inputs), outputs)


if __name__ == '__main__':
    unittest.main(verbosity=2)
