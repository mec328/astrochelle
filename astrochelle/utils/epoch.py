#!/usr/bin/env python
# ------------------------------------------------------------------------------
# epoch
# DESCRIPTION: all things timing
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-26
# REFERENCES:
#   [1] Vallado, David A. Fundamentals of astrodynamics and applications. 
#       First edition.
# ------------------------------------------------------------------------------

# Python imports
import numpy as np

# Astrochelle imports

# Constants
ALLOWED_TIME_SYSTEMS = ['UTC']
YYYY_MIN = -4713 # 4713 BC from Ref. 1, page 67

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
            time_system (`str`): time system representation to initialize in ('UTC')
            ---only some args below defined based on input type---
            year (`int`): TODO
            month (`int`): TODO
            day (`int`): TODO
            hours (`int`): TODO
            minutes (`int`): TODO
            seconds (`int`): TODO
            nanoseconds (`int`): TODO

        Attributes:
            time_system (`str`): time system representation to initialize in ('UTC')
            year (`int`): TODO
            month (`int`): TODO
            day (`int`): TODO
            hours (`int`): TODO
            minutes (`int`): TODO
            seconds (`int`): TODO
            nanoseconds (`int`): TODO
            
        '''
        if not time_system in ALLOWED_TIME_SYSTEMS:
            raise EpochException(msg = "Only UTC time supported right meow.") # obvious TODO lol

        self.time_system = time_system

        # Make sure that all required inputs are provided
        ymdhm = [year, month, day, hours, minutes] # TODO better name
        if None in ymdhm and not all([val is None for val in ymdhm]):
            raise EpochException(msg = "If providing ymdhms, must provide ALL components.")

        # TODO not sure if converting everything to this first before check
        flag_valid, msg = check_validity_date(
            year = year, month = month, day = day, hours = hours,
            minutes = minutes, seconds = seconds, nanoseconds = nanoseconds
            )

        if not flag_valid:
            assert EpochException(error_msg)

        # right now i realllllly don't care if this covers everything... i just want a simple representation of the epoch and associated 
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
        year (`int`): TODO
        month (`int`): TODO
        day (`int`): TODO
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


    return True, ""