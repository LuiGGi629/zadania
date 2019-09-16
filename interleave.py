def interleave(iterable1, iterable2):
    """Return iterable of one item at a time from each list."""
    interleaved = []
    for item1, item2 in zip(iterable1, iterable2):
        interleaved.append(item1)
        interleaved.append(item2)
    return interleaved
