from math import sqrt


def is_prime(candidate):
    """Return True if candidate number is prime."""
    return all(
        candidate % num != 0
        for num in range(2, int(sqrt(candidate)))
    )
