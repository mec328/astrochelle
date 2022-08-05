#!/usr/bin/env python
# ------------------------------------------------------------------------------
# absolute_state
# DESCRIPTION: supporting functions for astrodynamics (absolute state)
# AUTHOR: Michelle Chernick
# CREATED: 2022-08-04
# REFERENCES:
# ------------------------------------------------------------------------------

# Python imports

# Astrochelle imports
from astrochelle.utils.constants import SECONDS_IN_DAY, YEAR_MIN, DAYS_IN_MONTH, MJD_OFFSET

##################
# Error Handling #
##################


class AbsoluteState(Exception):
    '''Exceptions related to epoch
    '''

    def __init__(
        self,
        msg: str = "Something went wrong in absolute_state.py."
    ):

        super().__init__(msg)
