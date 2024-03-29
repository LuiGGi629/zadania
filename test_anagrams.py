import unittest
from anagrams import is_anagram


class IsAnagramTests(unittest.TestCase):
    """Tests for is_anagram."""
    def test_short_anagram(self):
        self.assertTrue(is_anagram("tea", "eat"))

    def test_different_lengths(self):
        self.assertFalse(is_anagram("tea", "treat"))

    def test_sink_skin(self):
        self.assertTrue(is_anagram("sink", "skin"))

    def test_same_letters_different_lengths(self):
        self.assertFalse(is_anagram("sinks", "skin"))

    def test_different_capitalization(self):
        self.assertTrue(is_anagram("Trey", "Yert"))
        self.assertTrue(is_anagram("Listen", "silent"))

    def test_spaces_ignored(self):
        phrase1 = "William Shakespeare"
        phrase2 = "I am a weakish speller"
        self.assertTrue(is_anagram(phrase1, phrase2))
        self.assertTrue(is_anagram("a b c", "a b d"))

    def test_punctuation_ignored(self):
        phrase1 = "A diet"
        phrase2 = "I'd eat"
        self.assertTrue(is_anagram(phrase1, phrase2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
