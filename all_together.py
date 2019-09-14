def all_together(*iterables):
    """String together all items from the given iterables."""
    return (
        item
        for iterable in iterables
        for item in iterable
    )
