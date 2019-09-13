def reverse_difference(numbers):
    """Return list subtracted from the reverse of itself."""
    return [
        n - m
        for n, m in zip(numbers, numbers[::-1])
    ]
