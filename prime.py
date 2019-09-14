def is_prime(candidate):
    """Return True if candidate number is prime."""
    if candidate < 2:
        return False
    for num in range(2, candidate):
        if candidate % num == 0:
            return False
    return True
