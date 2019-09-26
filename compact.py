def compact(iterable):
    """Return iterable with adjacent duplicate values removed."""
    deduplicated = []
    previous = object()
    # setting variable to a value that is only every equal to itself
    for item in iterable:
        if item != previous:
            deduplicated.append(item)
            previous = item
    return deduplicated
