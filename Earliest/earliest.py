def get_earliest(date1, date2):
    """Return earlies of two MM/DD/YYYY-formatted date strings."""
    month1 = date1[:2]
    day1 = date1[3:5]
    year1 = date1[6:]
    month2 = date2[:2]
    day2 = date2[3:5]
    year2 = date2[6:]

    ymd1 = year1 + month1 + day1
    ymd2 = year2 + month2 + day2

    if ymd1 < ymd2:
        return date1
    else:
        return date2
