def all_together(*iterables):
    """String together all items from the given iterables."""
    all_items = []
    for iterable in iterables:
        for item in iterable:
            all_items.append(item)
    return all_items
