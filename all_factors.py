from factors import get_factors


def get_all_factors(numbers):
    """Return a dictionary mapping numbers to their factors."""
    return {
        num: get_factors(num)
        for num in numbers
    }
