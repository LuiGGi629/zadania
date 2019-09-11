def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        row = []
        for n, m in zip(row1, row2):
            row.append(n + m)
        combined.append(row)
    return combined
