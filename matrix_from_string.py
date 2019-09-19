def matrix_from_string(string):
    """Convert rows of numbers to list of lists."""
    return [
        [int(x) for x in line.split()]
        for line in string.splitlines()
    ]
