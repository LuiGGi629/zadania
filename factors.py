def get_factors(number):
    """Return a list of all factors of the given number."""
    factors = []
    for num in range(1, number + 1):
        if number % num == 0:
            factors.append(num)
    return factors
