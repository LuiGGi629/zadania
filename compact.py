def compact(iterable):
    """Return iterable with adjacent duplicate values removed."""
    deduplicated = []
    previous = None
    # loop over iterable once and not depend on indexing
    for item in iterable:
        if item != previous:
            deduplicated.append(item)
            previous = item
    return deduplicated
    # this doesn't work because list starts with None values
