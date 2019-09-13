def transpose(matrix):
    """Return a transposed version of given list of lists."""
    transposed = []
    for row in zip(*matrix):
        transposed.append(list(row))
    return transposed
