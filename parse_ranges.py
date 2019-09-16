def parse_ranges(ranges_string):
    """Return a list of numbers corresponding to number ranges in a string."""
    pairs = (
        group.split("-")
        for group in ranges_string.split(",")
    )

    return (
        num
        for start, stop in pairs
        for num in range(int(start), int(stop) + 1)
    )
