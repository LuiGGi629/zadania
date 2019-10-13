def get_earliest(date1, date2):
    """Return earlies of two MM/DD/YYYY-formatted date strings."""
    date1_split = date1.split('/')
    date2_split = date2.split('/')
    month1 = date1_split[0]
    day1 = date1_split[1]
    year1 = date1_split[2]
    month2 = date2_split[0]
    day2 = date2_split[1]
    year2 = date2_split[2]

    ymd1 = year1 + month1 + day1
    ymd2 = year2 + month2 + day2

    if ymd1 < ymd2:
        return date1
    else:
        return date2
