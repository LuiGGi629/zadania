def flip_dict(dictionary):
    """Return a new dictionary that maps the original values to the keys."""
    flipped = {}
    for old_key, old_value in dictionary.items():
        flipped[old_value] = old_key
    return flipped
