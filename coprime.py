def coprime(number1, number2):
    """Return True if candidate numbers are coprime."""
    return not any(
        number1 % num == 0 and number2 % num == 0
        for num in range(2, min(number1, number2) + 1)
    )
