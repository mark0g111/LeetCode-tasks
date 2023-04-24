# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD,
# return the day number of the year.

import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        ymd = date.split('-')
        date1 = datetime.date(year=int(ymd[0]), month=int(ymd[1]), day=int(ymd[2]))
        date2 = datetime.date(year=int(ymd[0]), month=1, day=1)

        return (date1 - date2).days + 1
