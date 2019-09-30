def compact(iterable):
    """Return iterable with adjacent duplicate values removed."""
    previous = object()
    # setting variable to a value that is only every equal to itself
    for item in iterable:
        if item != previous:
            yield item
            previous = item
