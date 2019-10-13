from datetime import datetime


def get_earliest(string1, string2):
    """Return earlies of two MM/DD/YYYY-formatted date strings."""
    date1 = datetime.strptime(string1, "%m/%d/%Y")
    date2 = datetime.strptime(string2, "%m/%d/%Y")

    if date1 < date2:
        return string1
    else:
        return string2
