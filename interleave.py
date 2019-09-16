def interleave(iterable1, iterable2):
    """Return iterable of one item at a time from each list."""
    return (
        item
        for pair in zip(iterable1, iterable2)
        for item in pair
    )
