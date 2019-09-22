import random
from collections import namedtuple


def get_cards():
    """Create a list of namedtuples representing a deck of playing cards."""
    Card = namedtuple("Card", "rank suit")
    ranks = ["A"] + [str(n) for n in range(2, 11)] + ["J", "Q", "K"]
    suits = ["spades", "hearts", "diamonds", "clubs"]
    return [Card(rank, suit) for suit in suits for rank in ranks]


def shuffle_cards(deck):
    """Shuffles a deck in-place."""
    random.shuffle(deck)


def deal_cards(deck, count=2):
    """Remove the given number of cards from the deck and returns them."""
