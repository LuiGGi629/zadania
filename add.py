def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for rows in zip(*matrices):
        row = []
        for values in zip(*rows):
            total = 0
            for num in values:
                total += num
            row.append(total)
        combined.append(row)
    return combined
