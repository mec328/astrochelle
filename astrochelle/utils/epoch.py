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
# TODO:
#   Should probably eventually implement `iauDtf2d` from Ref. 3
#   This is the simplest implementation. May need more, including print format
# ------------------------------------------------------------------------------

# Python imports
from math import floor

# Astrochelle imports
from astrochelle.utils.constants import SECONDS_IN_DAY, YEAR_MIN, DAYS_IN_MONTH, MJD_OFFSET

# Constants
ALLOWED_TIME_SYSTEMS = ['UTC']

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
        seconds: float = None,
        mean_julian_day: float = None,
        day_fraction: float = None
    ):
        '''Time-keeping class

        Args:
            time_system (`str`): time system representation to initialize in
                see ALLOWED_TIME_SYSTEMS in `Constants` section
            ---only some args below defined based on input type---
            # TODO make a table in documentation about this
            year (`int`): calendar year
            month (`int`): calendar month as integer [1,12]
            day (`int`): calendar day
            hours (`int`): hours (24 hour format)
            minutes (`int`): minutes
            seconds (`float`): seconds
            mean_julian_day (`float`): mean julian day for zero hours
            day_fraction (`float`): fraction of day past zero hours

        Attributes:
            time_system (`str`): time system representation to initialize in
                see ALLOWED_TIME_SYSTEMS in `Constants` section
            mean_julian_day (`float`): mean julian day for zero hours
            day_fraction (`float`): fraction of day past zero hours

        '''
        if time_system not in ALLOWED_TIME_SYSTEMS:
            # obvious TODO lol
            raise EpochException(
                msg="See ALLOWED_TIME_SYSTEMS for currently supported systems."
            )

        self.time_system = time_system

        if mean_julian_day is not None:
            # Sweet, no conversions required!
            self.mean_julian_day = mean_julian_day
            self.day_fraction = 0 if day_fraction is None else day_fraction
            return

        # Make sure that all required inputs are provided
        ymdhm = [year, month, day, hours, minutes]  # TODO better name
        if None in ymdhm and not all([val is None for val in ymdhm]):
            raise EpochException(
                msg="If providing ymdhms, must provide ALL components.")

        # If seconds weren't provided, set to zero
        if seconds is None:
            seconds = 0

        # Check validity if inputted in calendar date format
        flag_valid, msg = check_validity_date(
            year=year, month=month, day=day, hours=hours,
            minutes=minutes, seconds=seconds
        )

        if not flag_valid:
            assert EpochException(msg)

        # Convert to MJD and day fraction
        self.mean_julian_day, self.day_fraction = to_mjd(
            year=year,
            month=month,
            day=day,
            hours=hours,
            minutes=minutes,
            seconds=seconds
        )

    def __add__(self, to_add):
        '''Overloaded addition operator, including rollover considerations
        (epoch+epoch)

        Args:
            to_add (`Epoch` or `float`): epoch or float you want to add
            to the current epoch
                if `float`, [s]

        Returns:
            `Epoch` result of addition
        '''
        if isinstance(to_add, float) or isinstance(to_add, int):
            # Float
            new_mjd = self.mean_julian_day
            new_day_fraction = self.day_fraction + to_add / SECONDS_IN_DAY

        else:
            # Epoch

            # Check that the time_systems are the same
            if self.time_system != to_add.time_system:
                raise EpochException(
                    f"Mismatch ({self.time_system},{to_add.time_system})")

            # Add the MJDs
            new_mjd = self.mean_julian_day + to_add.mean_julian_day

            # Add fractional days
            new_day_fraction = self.day_fraction + to_add.day_fraction

        # Account for rollover
        while new_day_fraction > 1:
            # Needs rollover
            new_day_fraction -= 1
            new_mjd += 1

        # Initialize new Epoch
        return Epoch(mean_julian_day=new_mjd, day_fraction=new_day_fraction)

    def __sub__(self, to_subtract):
        '''Overloaded subtraction operator, including rollover considerations
        (epoch+epoch)

        Args:
            to_subtract (`Epoch` or `float`): epoch or float you want to
            subtract from the current epoch
                if `float`, [s]

        Returns:
            `Epoch` result of addition
        '''
        if isinstance(to_subtract, float) or isinstance(to_subtract, int):
            # Float
            new_mjd = self.mean_julian_day
            new_day_fraction = self.day_fraction - to_subtract / SECONDS_IN_DAY

        else:
            # Epoch

            # Check that the time_systems are the same
            if self.time_system != to_subtract.time_system:
                raise EpochException(
                    f"Mismatch ({self.time_system},{to_subtract.time_system})")

            # Add the MJDs
            new_mjd = self.mean_julian_day - to_subtract.mean_julian_day

            # Add fractional days
            new_day_fraction = self.day_fraction - to_subtract.day_fraction

        # Account for rollover
        while new_day_fraction < 0:
            # Needs rollover
            new_day_fraction += 1
            new_mjd -= 1

        # Initialize new Epoch
        return Epoch(mean_julian_day=new_mjd, day_fraction=new_day_fraction)

########################
# Supporting Functions #
########################


def to_mjd(year: int = None,
           month: int = None,
           day: int = None,
           hours: int = None,
           minutes: int = None,
           seconds: float = None) -> tuple:
    '''Convert UTC time (saved) to Julian Date (JD)

    Args:
        year (`int`): calendar year
        month (`int`): calendar month as integer [1,12]
        day (`int`): calendar day
        hours (`int`): hours (24 hour format)
        minutes (`int`): minutes
        seconds (`float`): seconds 

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
    mo_scaled = int((month - 14) / 12)
    year_mo_scaled = int(year + mo_scaled)

    mean_julian_day = (
        (int((1461 * (year_mo_scaled + 4800)) / 4)
         + int((367 * int((month - 2 - 12 * mo_scaled))) / 12)
         - int((3 * ((year_mo_scaled + 4900) / 100)) / 4)
         + int(day) - 2432076)
    )
    day_fraction = (hours + minutes/60 + seconds/3600)/24

    return (mean_julian_day, day_fraction)


def to_jd(
        year: int = None,
        month: int = None,
        day: int = None,
        hours: int = None,
        minutes: int = None,
        seconds: float = None) -> float:
    '''Convert UTC time (saved) to Mean Julian Date (MJD)

    Args:
        year (`int`): calendar year
        month (`int`): calendar month as integer [1,12]
        day (`int`): calendar day
        hours (`int`): hours (24 hour format)
        minutes (`int`): minutes
        seconds (`float`): seconds

    Modifies:
        None (TODO? mb i want this to be an attribute)

    Returns:
        JD (`float`)
    '''

    mean_julian_day, day_fraction = to_mjd(
        year=year,
        month=month,
        day=day,
        hours=hours,
        minutes=minutes,
        seconds=seconds
    )
    return mean_julian_day + day_fraction + MJD_OFFSET


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
        hours(`int`): hours (24 hour format)
        minutes(`int`): minutes
        seconds(`float`): seconds

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
