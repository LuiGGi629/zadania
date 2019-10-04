from collections import Counter


def count_words(string):
    """Return the number of items each word occurs in the string."""
    words = []
    for word in string.lower().split():
        words.append(word.strip(',.?";!()¿'))
    return Counter(words)
