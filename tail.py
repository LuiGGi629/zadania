def tail(iterable, n):
    """Return the last n items of given sentence."""
    items = []
    if n == 1:
        for item in iterable:
            items = [item]
    elif n > 0:
        for item in iterable:
            items = [*items[-n+1:], item]
    return items
