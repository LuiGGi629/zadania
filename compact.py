def compact(sequence):
    """Return iterable with adjacent duplicate values removed."""
    deduplicated = []
    for i, item in enumerate(sequence):
        # use indexes to check whether the current item is the same as before
        if i == 0 or item != sequence[i-1]:
            # appending item 0 and then only appending subsequent items
            # if they are not equal to the item just before their index
            deduplicated.append(item)
    return deduplicated
