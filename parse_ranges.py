def parse_ranges(ranges_string):
    """Return a list of numbers corresponding to number ranges in a string."""
    numbers = []
    for group in ranges_string.split(","):
        start, stop = group.split("-")
        for num in range(int(start), int(stop) + 1):
            numbers.append(num)
    return numbers
