from collections import Counter


def count_words(string):
    """Return the number of items each word occurs in the string."""
    return Counter(string.split())
