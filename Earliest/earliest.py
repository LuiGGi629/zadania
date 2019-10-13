def get_earliest(date1, date2):
    """Return earlies of two MM/DD/YYYY-formatted date strings."""
    month1, day1, year1 = date1.split('/')
    month2, day2, year2 = date2.split('/')

    if (year1, month1, day1) < (year2, month2, day2):
        return date1
    else:
        return date2
