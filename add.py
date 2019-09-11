def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for rows in zip(*matrices):
        row = []
        for values in zip(*rows):
            row.append(sum(values))
        combined.append(row)
    return combined
