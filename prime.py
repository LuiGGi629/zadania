def is_prime(candidate):
    """Return True if candidate number is prime."""
    return candidate >= 2 and all(
        candidate % num != 0
        for num in range(2, candidate)
    )
