import unittest
from collections import namedtuple
from deal_cards import deal_cards, shuffle_cards, get_cards


class GetCardsTest(unittest.TestCase):
    """Tests for get_cards."""
    def test_get_cards(self):
        Card = namedtuple("Card", "rank suit")

        deck = [
                Card(rank="A", suit="spades"), Card(rank="2", suit="spades"),
                Card(rank="3", suit="spades"), Card(rank="4", suit="spades"),
                Card(rank="5", suit="spades"), Card(rank="6", suit="spades"),
                Card(rank="7", suit="spades"), Card(rank="8", suit="spades"),
                Card(rank="9", suit="spades"), Card(rank="10", suit="spades"),
                Card(rank="J", suit="spades"), Card(rank="Q", suit="spades"),
                Card(rank="K", suit="spades"), Card(rank="A", suit="hearts"),
                Card(rank="2", suit="hearts"), Card(rank="3", suit="hearts"),
                Card(rank="4", suit="hearts"), Card(rank="5", suit="hearts"),
                Card(rank="6", suit="hearts"), Card(rank="7", suit="hearts"),
                Card(rank="8", suit="hearts"), Card(rank="9", suit="hearts"),
                Card(rank="10", suit="hearts"), Card(rank="J", suit="hearts"),
                Card(rank="Q", suit="hearts"), Card(rank="K", suit="hearts"),
                Card(rank="A", suit="diamonds"),
                Card(rank="2", suit="diamonds"),
                Card(rank="3", suit="diamonds"),
                Card(rank="4", suit="diamonds"),
                Card(rank="5", suit="diamonds"),
                Card(rank="6", suit="diamonds"),
                Card(rank="7", suit="diamonds"),
                Card(rank="8", suit="diamonds"),
                Card(rank="9", suit="diamonds"),
                Card(rank="10", suit="diamonds"),
                Card(rank="J", suit="diamonds"),
                Card(rank="Q", suit="diamonds"),
                Card(rank="K", suit="diamonds"),
                Card(rank="A", suit="clubs"), Card(rank="2", suit="clubs"),
                Card(rank="3", suit="clubs"), Card(rank="4", suit="clubs"),
                Card(rank="5", suit="clubs"), Card(rank="6", suit="clubs"),
                Card(rank="7", suit="clubs"), Card(rank="8", suit="clubs"),
                Card(rank="9", suit="clubs"), Card(rank="10", suit="clubs"),
                Card(rank="J", suit="clubs"), Card(rank="Q", suit="clubs"),
                Card(rank="K", suit="clubs"),
                ]

        self.assertEqual(get_cards(), deck)


class ShuffleTest(unittest.TestCase):
    """Tests for shuffle_cards."""
    def test_shuffle(self):
        things = [1, 2, 3, 4, 5]
        original = list(things)
        shuffle_cards(things)
        self.assertNotEqual(original, things)
        self.assertEqual(set(original), set(things))


class DealCardsTest(unittest.TestCase):
    """Tests for deal_cards."""
    def test_deal_cards(self):
        Card = namedtuple("Card", "rank suit")

        deck = [
                Card(rank="A", suit="spades"), Card(rank="2", suit="spades"),
                Card(rank="3", suit="spades"), Card(rank="4", suit="spades"),
                Card(rank="5", suit="spades"), Card(rank="6", suit="spades"),
                Card(rank="7", suit="spades"), Card(rank="8", suit="spades"),
                Card(rank="9", suit="spades"), Card(rank="10", suit="spades"),
                Card(rank="J", suit="spades"), Card(rank="Q", suit="spades"),
                Card(rank="K", suit="spades"), Card(rank="A", suit="hearts"),
                Card(rank="2", suit="hearts"), Card(rank="3", suit="hearts"),
                Card(rank="4", suit="hearts"), Card(rank="5", suit="hearts"),
                Card(rank="6", suit="hearts"), Card(rank="7", suit="hearts"),
                Card(rank="8", suit="hearts"), Card(rank="9", suit="hearts"),
                Card(rank="10", suit="hearts"), Card(rank="J", suit="hearts"),
                Card(rank="Q", suit="hearts"), Card(rank="K", suit="hearts"),
                Card(rank="A", suit="diamonds"),
                Card(rank="2", suit="diamonds"),
                Card(rank="3", suit="diamonds"),
                Card(rank="4", suit="diamonds"),
                Card(rank="5", suit="diamonds"),
                Card(rank="6", suit="diamonds"),
                Card(rank="7", suit="diamonds"),
                Card(rank="8", suit="diamonds"),
                Card(rank="9", suit="diamonds"),
                Card(rank="10", suit="diamonds"),
                Card(rank="J", suit="diamonds"),
                Card(rank="Q", suit="diamonds"),
                Card(rank="K", suit="diamonds"),
                Card(rank="A", suit="clubs"), Card(rank="2", suit="clubs"),
                Card(rank="3", suit="clubs"), Card(rank="4", suit="clubs"),
                Card(rank="5", suit="clubs"), Card(rank="6", suit="clubs"),
                Card(rank="7", suit="clubs"), Card(rank="8", suit="clubs"),
                Card(rank="9", suit="clubs"), Card(rank="10", suit="clubs"),
                Card(rank="J", suit="clubs"), Card(rank="Q", suit="clubs"),
                Card(rank="K", suit="clubs"),
                ]

        hand = [Card(rank="A", suit="spades"), Card(rank="J", suit="hearts")]

        self.assertEqual(deal_cards(deck), hand)


if __name__ == '__main__':
    unittest.main(verbosity=2)
