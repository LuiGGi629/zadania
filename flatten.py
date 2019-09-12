def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [
        item
        for row in matrix
        for item in row
    ]
