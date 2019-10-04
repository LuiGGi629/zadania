from collections import defaultdict


def count_words(string):
    """Return the number of items each word occurs in the string."""
    count = defaultdict(int)
    for word in string.split():
        count[word] += 1
    return count
