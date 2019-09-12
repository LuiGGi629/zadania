import unittest
from power import power_list


class PowerListTests(unittest.TestCase):
    """Tests for power_list."""
    def test_integers(self):
        self.assertEqual(power_list([6, 9, 69]), [1, 9, 4761])

    def test_floats(self):
        inputs = [78, 700, 82, 16, 2, 3, 9.5]
        outputs = [1, 700, 6724, 4096, 16, 243, 735091.890625]
        self.assertEqual(power_list(inputs), outputs)


if __name__ == '__main__':
    unittest.main()
