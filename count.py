def count_words(string):
    """Return the number of items each word occurs in the string."""
    count = {}
    for word in string.split():
        count[word] = count.get(word, 0) + 1
    return count
