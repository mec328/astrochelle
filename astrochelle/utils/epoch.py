#!/usr/bin/env python
# ------------------------------------------------------------------------------
# epoch
# DESCRIPTION: all things timing
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-26
# REFERENCES:
#   [1] Vallado, David A. Fundamentals of astrodynamics and applications.
#       First edition.
#   [2] Eugene Yarmash. "How to determine whether a year is a leap year?".
#       https://stackoverflow.com/q/11621740
#   [3] Software Routines from the IAU SOFA Collection were used.
#       Copyright International Astronomical Union Standards of Fundamental
#       Astronomy (http://www.iausofa.org)”.
#       Documentation: https://www.iausofa.org/2021_0512_C/sofa/sofa_ts_c.pdf
# ------------------------------------------------------------------------------

# Python imports
import numpy as np
from math import floor

# Astrochelle imports

# Constants
ALLOWED_TIME_SYSTEMS = ['UTC']
YEAR_MIN = -4713  # 4713 BC from Ref. 1, page 67
DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}  # Definitely had to do the song to get these
MJD_OFFSET = 2400000.5  # TODO constants file

##################
# Error Handling #
##################


class EpochException(Exception):
    '''Exceptions related to epoch
    '''

    def __init__(
        self,
        msg: str = "Something went wrong in epoch.py."
    ):

        super().__init__(msg)


#########
# Epoch #
#########
class Epoch():
    def __init__(
        self,
        time_system: str = 'UTC',
        *,
        year: int = None,
        month: int = None,
        day: int = None,
        hours: int = None,
        minutes: int = None,
        seconds: float = None

    ):
        '''Time-keeping class

        Args:
            time_system (`str`): time system representation to initialize in
                see ALLOWED_TIME_SYSTEMS in `Constants` section
            ---only some args below defined based on input type---
            year (`int`): calendar year
            month (`int`): calendar month as integer [1,12]
            day (`int`): calendar day
            hours (`int`): TODO
            minutes (`int`): TODO
            seconds (`float`): TODO

        Attributes:
            time_system (`str`): time system representation to initialize in
                see ALLOWED_TIME_SYSTEMS in `Constants` section
            year (`int`): calendar year
            month (`int`): calendar month as integer [1,12]
            day (`int`): calendar day
            hours (`int`): TODO
            minutes (`int`): TODO
            seconds (`float`): TODO

        '''
        if time_system not in ALLOWED_TIME_SYSTEMS:
            # obvious TODO lol
            raise EpochException(msg="Only UTC time supported right meow.")

        self.time_system = time_system

        # Make sure that all required inputs are provided
        ymdhm = [year, month, day, hours, minutes]  # TODO better name
        if None in ymdhm and not all([val is None for val in ymdhm]):
            raise EpochException(
                msg="If providing ymdhms, must provide ALL components.")

        # If seconds weren't provided, set to zero
        if seconds is None:
            seconds = 0

        # TODO not sure if converting everything to this first before check
        flag_valid, msg = check_validity_date(
            year=year, month=month, day=day, hours=hours,
            minutes=minutes, seconds=seconds
        )

        if not flag_valid:
            assert EpochException(msg)

        # TODO more stuff

        # Looks good! Save things
        self.year = year
        self.month = month
        self.day = day
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_mjd(self) -> tuple:
        '''Convert UTC time (saved) to Julian Date (JD)

        Args:
            None

        Modifies:
            None (TODO? mb i want this to be an attribute)

        Returns:
            tuple
                MJD (`float`) for zero hours (aka day number)
                day_fraction (`float`): fraction of day past zero hours

        Notes:
            Adapted from iauCal2jd in Ref. 3
        '''

        # Compute scaled month (See pages 67-68 in Ref. 1)
        mo_scaled = int((self.month - 14) / 12)
        year_mo_scaled = int(self.year + mo_scaled)

        mean_julian_day = (
            (int((1461 * (year_mo_scaled + 4800)) / 4)
             + int((367 * int((self.month - 2 - 12 * mo_scaled))) / 12)
             - int((3 * ((year_mo_scaled + 4900) / 100)) / 4)
             + int(self.day) - 2432076)
        )
        day_fraction = (self.hours + self.minutes/60 + self.seconds/3600)/24

        return (mean_julian_day, day_fraction)

    def to_jd(self) -> float:
        '''Convert UTC time (saved) to Mean Julian Date (MJD)

        Args:
            None

        Modifies:
            None (TODO? mb i want this to be an attribute)

        Returns:
            JD (`float`)
        '''

        mean_julian_day, day_fraction = self.to_mjd()
        return mean_julian_day + day_fraction + MJD_OFFSET

########################
# Supporting Functions #
########################


def check_validity_date(
        year: int = None,
        month: int = None,
        day: int = None,
        hours: int = None,
        minutes: int = None,
        seconds: float = None) -> tuple:
    '''Check that the inputted date vector makes sense

    Args:
        year(`int`): calendar year
        month(`int`): calendar month as integer[1, 12]
        day(`int`): calendar day
        hours(`int`): TODO
        minutes(`int`): TODO
        seconds(`float`): TODO

    Returns:
        tuple
            True if valid, False else
            msg(`str`): empty string if date was valid, else failure reason
    '''
    # Check that year is not before YEAR_MIN
    if year < YEAR_MIN:
        return False, f"Provided year {year} is less than {YEAR_MIN}."

    # Check that month is real
    if month < 1 or month > 12:
        return False, f"Provided month {month} is outside of the range [1,12]."

    # Check that day is valid given month
    days_in_month = DAYS_IN_MONTH[month]
    if month == 2 and check_leap_year(year=year):
        # It's a leap year, add one day to February
        days_in_month += 1

    if day < 0 or day > days_in_month:
        return False, f"Provided day {day} not in month {month}."

    # Check that minutes and hours are non-negative
    if hours < 0 or minutes < 0 or seconds < 0:
        return False, "Provided hours, minutes, or seconds negative."

    # Check that minutes, hours, seconds provide are less than a fraction of a
    # day
    day_fraction = (hours + minutes/60 + seconds/3600)/24
    if day_fraction > 1:
        return False, f"Day fraction {day_fraction} greater than a day."

    return True, ""


def check_leap_year(year: int) -> bool:
    '''Check if it's a leap year

    Args:
        year(`int`): calendar year

    Returns:
        True if leap year, False else

    Notes:
        from Ref. [2]
    '''
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        # it's a leap year!
        return True

    return False
