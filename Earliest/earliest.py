def get_earliest(*dates):
    """Return earliest of two MM/DD/YYYY-formatted date strings.
    Providing a key keyword argument. Key function tells the min function
    what criteria determining whether one date string is less than
    (earlier than) another one. The key function will be called with
    each date string and the returned date string will be the one
    with resulting key tuple which is smalles."""
    def date_key(date):
        (month, day, year) = date.split('/')
        # split and rearrange each date string
        return (year, month, day)
    return min(dates, key=date_key)  # find out which one is the earliest
