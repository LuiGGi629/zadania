def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]
