#!/usr/bin/env python
# ------------------------------------------------------------------------------
# absolute_state
# DESCRIPTION: supporting functions for astrodynamics (absolute state)
# AUTHOR: Michelle Chernick
# CREATED: 2022-08-04
# REFERENCES:
# ------------------------------------------------------------------------------

# Python imports
from math import sqrt

# Astrochelle imports
from astrochelle.utils.constants import GM_EARTH

##################
# Error Handling #
##################


class AbsoluteStateException(Exception):
    '''Exceptions related to epoch
    '''

    def __init__(
        self,
        msg: str = "Something went wrong in absolute_state.py."
    ):

        super().__init__(msg)


def calculate_mean_motion(semimajor_axis: float) -> float:
    '''Calculate the mean motion of a Keplerian orbit

    Args:
        semimajor_axis (`float`): semi-major axis of the orbit [m]

    Returns:
        mean motion (`float`)
    '''
    return sqrt(GM_EARTH / semimajor_axis**3)
