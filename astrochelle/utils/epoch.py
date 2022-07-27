#!/usr/bin/env python
# ------------------------------------------------------------------------------
# epoch
# DESCRIPTION: all things timing
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-26
# ------------------------------------------------------------------------------

# Python imports
import numpy as np

# Astrochelle imports

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

        # right now i realllllly don't care if this covers everything... i just want a simple representation of the epoch and associated 
        # overwritten math funcs
