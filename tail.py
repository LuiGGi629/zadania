def tail(iterable, n):
    """Return the last n items of given sentence."""
    items = []
    if n <= 0:
        return []
    for item in iterable:
        items = [*items[-(n-1):], item]
    return items
