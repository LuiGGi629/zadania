import unittest
from ascii import get_ascii_codes


class GetASCIICodeTest(unittest.TestCase):
    """Tests for get_ascii_codes."""
    def test_multiple_words(self):
        words = ["hello", "bye", "yes", "no", "python"]
        outputs = {
            "yes": [121, 101, 115],
            "hello": [104, 101, 108, 108, 111],
            "python": [112, 121, 116, 104, 111, 110],
            "no": [110, 111],
            "bye": [98, 121, 101],
        }
        self.assertEqual(get_ascii_codes(words), outputs)


if __name__ == '__main__':
    unittest.main(verbosity=2)
