import unittest
from transliterate import transliterate


class TransliterateTests(unittest.TestCase):
    """Tests for transliterate."""
    def test_rat(self):
        self.assertEqual(transliterate("rato"), "rat")

    def test_the_rat(self):
        self.assertEqual(transliterate("el rato"), "the rat")

    def test_rat_in_house(self):
        inputs = "el rato esta en la casa"
        outputs = "the rat is in the house"
        self.assertEqual(transliterate(inputs), outputs)


if __name__ == '__main__':
    unittest.main(verbosity=2)
