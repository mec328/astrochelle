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
# ------------------------------------------------------------------------------

# Python imports
import numpy as np

# Astrochelle imports

# Constants
ALLOWED_TIME_SYSTEMS = ['UTC']
YYYY_MIN = -4713  # 4713 BC from Ref. 1, page 67
DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}  # Definitely had to do the song to get these

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
        seconds: int = None,
        nanoseconds: int = None

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
            seconds (`int`): TODO
            nanoseconds (`int`): TODO

        Attributes:
            time_system (`str`): time system representation to initialize in
                see ALLOWED_TIME_SYSTEMS in `Constants` section
            year (`int`): calendar year
            month (`int`): calendar month as integer [1,12]
            day (`int`): calendar day
            hours (`int`): TODO
            minutes (`int`): TODO
            seconds (`int`): TODO
            nanoseconds (`int`): TODO

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

        # TODO not sure if converting everything to this first before check
        flag_valid, msg = check_validity_date(
            year=year, month=month, day=day, hours=hours,
            minutes=minutes, seconds=seconds, nanoseconds=nanoseconds
        )

        if not flag_valid:
            assert EpochException(msg)

        # right now i realllllly don't care if this covers everything...
        # i just want a simple representation of the epoch and associated
        # overwritten math funcs

########################
# Supporting Functions #
########################


def check_validity_date(
        year: int = None,
        month: int = None,
        day: int = None,
        hours: int = None,
        minutes: int = None,
        seconds: int = None,
        nanoseconds: int = None)->tuple:
    '''Check that the inputted date vector makes sense

    Args:
        year (`int`): calendar year
        month (`int`): calendar month as integer [1,12]
        day (`int`): calendar day
        hours (`int`): TODO
        minutes (`int`): TODO
        seconds (`int`): TODO
        nanoseconds (`int`): TODO      

    Returns:
        tuple
            True if valid, False else
            msg (`str`): empty string if date was valid, else failure reason
    '''
    # Check that year is not before YYYY_MIN
    if year < YYYY_MIN:
        return False, f"Provided year {year} is less than {YYYY_MIN}."

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

    # Check that minutes, seconds, nanoseconds are valid and scale them
    # (TODO probs more functions)
    # if seconds nano seconds provided

    return True, ""


def check_leap_year(year: int)->bool:
    '''Check if it's a leap year

    Args:
        year (`int`): calendar year

    Returns:
        True if leap year, False else

    Notes:
        from Ref. [2]
    '''
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        # it's a leap year!
        return True

    return False
