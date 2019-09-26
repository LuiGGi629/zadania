def compact(iterable):
    """Return iterable with adjacent duplicate values removed."""
    sequence = list(iterable)
    # converting incoming iterable to a list
    deduplicated = []
    # this isn't very efficient -> creating a new list
    # just to loop over it once and discard it
    for i, item in enumerate(sequence):
        if i == 0 or item != sequence[i-1]:
            deduplicated.append(item)
    return deduplicated
