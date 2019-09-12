import unittest
from vowel import get_vowel_names


class GetVowelNamesTests(unittest.TestCase):
    """Tests for get_vowel_names."""
    def test_one_vowel_name(self):
        names = ["Ala", "Franek", "Celina", "Juliusz"]
        self.assertEqual(get_vowel_names(names), ["Ala"])

    def test_multiple_vowel_names(self):
        names = ["Edek", "Artur", "Szczepan", "Mariusz"]
        self.assertEqual(get_vowel_names(names), ["Edek", "Artur"])

    def test_empty(self):
        self.assertEqual(get_vowel_names([]), [])


if __name__ == '__main__':
    unittest.main()
