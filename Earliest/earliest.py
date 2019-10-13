import re


def get_earliest(date1, date2):
    """Return earlies of two MM/DD/YYYY-formatted date strings."""
    DATE_RE = re.compile(r'^(\d{2})/(\d{2})/(\d{4}$)')
    (month1, day1, year1) = DATE_RE.search(date1).groups()
    (month2, day2, year2) = DATE_RE.search(date2).groups()

    return date1 if (year1, month1, day1) < (year2, month2, day2) else date2
