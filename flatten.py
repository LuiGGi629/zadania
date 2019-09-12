def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    flattened = []
    for row in matrix:
        for item in row:
            flattened.append(item)
    return flattened
