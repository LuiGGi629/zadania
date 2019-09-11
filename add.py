def get_shape(matrix):
    return [len(r) for r in matrix]


def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    shape_of_matrix = get_shape(matrices[0])
    if any(get_shape(m) != shape_of_matrix for m in matrices):
        raise ValueError("Given matrices are not the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]
