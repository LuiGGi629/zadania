def tail(sequence, n):
    """Return the last n items of given sentence."""
    if n <= 0:
        return []
    return list(sequence[-n:])
