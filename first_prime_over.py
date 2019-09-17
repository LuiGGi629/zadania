from prime import is_prime


def first_prime_over(number):
    """Return the first prime number over a given number."""
    primes = (
        number
        for number in range(number + 1, number**2)
        if is_prime(number)
    )
    return next(primes)
