def get_earliest(date1, date2):
    """Return earlies of two MM/DD/YYYY-formatted date strings."""
    month1 = date1[:2]
    day1 = date1[3:5]
    year1 = date1[6:]
    month2 = date2[:2]
    day2 = date2[3:5]
    year2 = date2[6:]

    if year1 < year2:
        return date1
    elif year1 > year2:
        return date2
    elif month1 < month2:
        return date1
    elif month1 > month2:
        return date2
    elif day1 < day2:
        return date1
    elif day1 > day2:
        return date2
    else:
        return date1
