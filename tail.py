def tail(iterable, n):
    """Return the last n items of given sentence."""
    items = []
    if n <= 0:
        return []
    elif n == 1:
        index = slice(0, 0)
    else:
        index = slice(-(n-1), None)
    for item in iterable:
        items = [*items[index], item]
    return items
