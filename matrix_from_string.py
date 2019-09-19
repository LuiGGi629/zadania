def matrix_from_string(string):
    """Convert rows of numbers to list of lists."""
    matrix = []
    for line in string.splitlines():
        matrix.append([int(x) for x in line.split()])
    return matrix
