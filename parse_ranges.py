def parse_ranges(ranges_string):
    """Return a list of numbers corresponding to number ranges in a string."""
    pairs = []
    for group in ranges_string.split(","):
        pairs.append(group.split("-"))
    numbers = []
    for start, stop in pairs:
        for num in range(int(start), int(stop) + 1):
            numbers.append(num)
    return numbers
