def is_prime(candidate):
    """Return True if candidate number is prime."""
    return candidate >= 2 and not any(
        candidate % num == 0
        for num in range(2, candidate)
    )
