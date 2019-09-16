def interleave(iterable1, iterable2):
    """Return iterable of one item at a time from each list."""
    interleaved = []
    for pair in zip(iterable1, iterable2):
        for item in pair:
            interleaved.append(item)
    return interleaved
