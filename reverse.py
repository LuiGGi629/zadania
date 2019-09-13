def reverse_difference(numbers):
    """Return list subtracted from the reverse of itself."""
    differences = []
    for n, m in zip(numbers, numbers[::-1]):
        differences.append(n - m)
    return differences
