def power_list(numbers):
    """Return a list that contains each number raised to the i-th power."""
    return [
        num**i
        for i, num in enumerate(numbers)
    ]
