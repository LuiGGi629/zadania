def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    matrix_shape = {
        tuple(len(r) for r in matrix)
        for matrix in matrices
    }
    if len(matrix_shape) > 1:
        raise ValueError("Given matrices are not the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]
