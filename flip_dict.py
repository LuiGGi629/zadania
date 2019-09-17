def flip_dict(dictionary):
    """Return a new dictionary that maps the original values to the keys."""
    return {
        old_value: old_key
        for old_key, old_value in dictionary.items()
    }
