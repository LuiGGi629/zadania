def tail(iterable, n):
    """Return the last n items of given sentence."""
    items = []
    if n <= 0:
        return []
    elif n == 1:
        # slice object is what Python creates when U use slicing notation
        index = slice(0, 0)
        # when U say sequence[-n:] == sequence[slice(-n, None)]
    else:
        index = slice(-(n-1), None)
    for item in iterable:
        items = [*items[index], item]
    return items
