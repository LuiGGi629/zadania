def matrix_from_string(string):
    """Convert rows of numbers to list of lists."""
    matrix = []
    for line in string.splitlines():
        row = []
        for x in line.split():
            row.append(int(x))
        matrix.append(row)
    return matrix
