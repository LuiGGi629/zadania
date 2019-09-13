def transpose(matrix):
    """Return a transposed version of given list of lists."""
    return [
        list(row)
        for row in zip(*matrix)
    ]
