def compact(sequence):
    """Return iterable with adjacent duplicate values removed."""
    deduplicated = []
    # zip together the original sequence with itself shifted by one
    # so that the each item can compare itself with the one before
    for item, previous in zip(sequence, [object(), *sequence]):
        # *"unpacking" each of the items into new list, after object()
        if item != previous:
            deduplicated.append(item)
    return deduplicated
