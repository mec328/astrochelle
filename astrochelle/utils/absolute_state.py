#!/usr/bin/env python
# ------------------------------------------------------------------------------
# absolute_state
# DESCRIPTION: supporting functions for astrodynamics (absolute state)
# AUTHOR: Michelle Chernick
# CREATED: 2022-08-04
# REFERENCES:
#   [1] Vallado, David A. Fundamentals of astrodynamics and applications.
#       First edition.
# ------------------------------------------------------------------------------

# Python imports
from math import sqrt
import numpy as np

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


def convert_anomaly_mean_to_eccentric(semimajor_axis: float, eccentricity: float) -> float:
    '''TODO

    Args:
        semimajor_axis (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        TODO
    '''
    return


def convert_anomaly_eccentric_to_true(semimajor_axis: float, eccentricity: float) -> float:
    '''TODO

    Args:
        semimajor_axis (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        TODO
    '''
    return


def convert_anomaly_true_to_eccentric(semimajor_axis: float, eccentricity: float) -> float:
    '''TODO

    Args:
        semimajor_axis (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        TODO
    '''
    return


def convert_anomaly_eccentric_to_mean(semimajor_axis: float, eccentricity: float) -> float:
    '''TODO

    Args:
        semimajor_axis (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        TODO
    '''
    return


def convert_anomaly_mean_to_true(semimajor_axis: float, eccentricity: float) -> float:
    '''TODO

    Args:
        semimajor_axis (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        TODO
    '''
    return


def convert_anomaly_true_to_mean(semimajor_axis: float, eccentricity: float) -> float:
    '''TODO

    Args:
        semimajor_axis (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        TODO
    '''
    return


def construct_gve_matrix(koe: np.array) -> np.ndarray:
    '''Construct GVE matrix which represents the transition between
    accelerations in RTN to variations in the OE

    Args:
        koe(`np.array`): Keplerian orbit elements[m, rad]

    Returns:
        GVE matrix(6x3)

    Source:
        Ref. 1 page 567 (Eq. 8-24)
    '''
    gve_matrix = np.zeros((6, 3))

    # Extract OE
    a = koe[0]
    e = koe[1]
    i = koe[2]
    W = koe[3]
    w = koe[4]
    M = koe[5]

    # Compute mean motion
    mean_motion = calculate_mean_motion(semimajor_axis=a)

    # Convert mean anomaly to true
    nu = convert_anomaly_mean_to_true(semimajor_axis=a, eccentricity=e)

    # TODO

    return gve_matrix
