from itertools import groupby


def compact(iterable):
    """Return iterable with adjacent duplicate values removed."""
    return (
        item
        for item, group in groupby(iterable)
        # groupby function groups consecutive items
        # in an iterable that are equivalent
    )
