from collections import Counter
import re


def count_words(string):
    """Return the number of items each word occurs in the string."""
    return Counter(re.findall(r"\b[\w'-]+\b", string.lower()))
