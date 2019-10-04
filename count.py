def count_words(string):
    """Return the number of items each word occurs in the string."""
    count = {}
    for word in string.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
