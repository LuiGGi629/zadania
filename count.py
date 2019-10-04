def count_words(string):
    """Return the number of items each word occurs in the string."""
    count = {}
    for word in string.split():
        count.setdefault(word, 0)
        count[word] += 1
    return count
