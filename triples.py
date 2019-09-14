def triples(num):
    """Return list of Pythagorean triples less than input num."""
    return [
        (a, b, c)
        for a in range(1, num)
        for b in range(a + 1, num)
        for c in range(b + 1, num)
        if a**2 + b**2 == c**2
    ]
