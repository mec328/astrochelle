#!/usr/bin/env python
# ------------------------------------------------------------------------------
# math
# DESCRIPTION: math functions and shiet
# AUTHOR: Michelle Chernick
# CREATED: 2022-08-05
# REFERENCES:
# ------------------------------------------------------------------------------

# Python imports
from math import pi

# Astrochelle imports

##################
# Error Handling #
##################


class MathException(Exception):
    '''Exceptions related to module_name
    '''

    def __init__(
        self,
        msg: str = "Something went wrong in math.py."
    ):

        super().__init__(msg)


def wrap_0_to_2pi(angle: float) -> float:
    '''Wrap an angle to lie within 0 and 2pi

    Args:
        angle (`float`): angle to wrap

    Returns:
        wrapped angle (`float`)
    '''
    while angle < 0:
        angle += 2*pi
    while angle > 2*pi:
        angle -= 2*pi

    return angle
