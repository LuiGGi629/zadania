from collections import deque


def tail(iterable, n):
    """Return the last n items of given sentence."""
    if n <= 0:
        return []
    items = deque(maxlen=n)
    for item in iterable:
        items.append(item)
    return list(items)
