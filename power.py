def power_list(numbers):
    """Return a list that contains each number raised to the i-th power."""
    powers = []
    for i, num in enumerate(numbers):
        powers.append(num**i)
    return powers
