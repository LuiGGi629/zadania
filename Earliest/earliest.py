def get_earliest(date1, date2):
    """Return earlies of two MM/DD/YYYY-formatted date strings."""
    if date1[6:] < date2[6:]:
        return date1
    elif date1[6:] > date2[6:]:
        return date2
    elif date1[2:] < date2[2:]:
        return date1
    elif date1[2:] > date2[2:]:
        return date2
    elif date1[3:5] < date2[3:5]:
        return date1
    elif date1[3:5] > date2[3:5]:
        return date2
    else:
        return date1
