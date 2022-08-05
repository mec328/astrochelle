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
from math import sqrt, sin, tan, atan, cos, pi
import numpy as np

# Astrochelle imports
from astrochelle.utils.constants import GM_EARTH
from astrochelle.utils.math import wrap_0_to_2pi

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


def convert_anomaly_mean_to_eccentric(
        mean_anomaly: float,
        eccentricity: float,
        tolerance: float = 1e-8,
        allowed_iterations: int = 50
) -> float:
    '''Convert the mean anomaly to eccentric anomaly

    Args:
        mean_anomaly (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit
        tolerance (`float`): convergence tolerance to stop iterations
        allowed_iterations (`int`): number of iterations allowed

    Returns:
        eccentric anomaly (`float`)

    Source:
        Ref. 1 page 211
    '''

    # Wrap provided mean anomaly to lie between 0 and 2pi
    mean_anomaly_aug = wrap_0_to_2pi(mean_anomaly)

    # TODO explain
    eccentric_anomaly = pi if eccentricity >= 0.8 else mean_anomaly_aug

    # Initialize error value using the expression in Algorithm 25 in Ref. 1
    # (page 232)
    eccentric_anomaly_iter = eccentric_anomaly + \
        (mean_anomaly_aug - convert_anomaly_eccentric_to_mean(
            eccentric_anomaly,
            eccentricity))/(1-eccentricity*cos(eccentric_anomaly))

    num_iterations = 0
    while num_iterations < allowed_iterations and abs(
            eccentric_anomaly_iter - eccentric_anomaly) >= tolerance:
        # Save last iteration's eccentric anomaly value
        eccentric_anomaly = eccentric_anomaly_iter

        # Re-calculate eccentric anomaly using same Algorithm
        eccentric_anomaly_iter = eccentric_anomaly + \
            (mean_anomaly_aug - convert_anomaly_eccentric_to_mean(
                eccentric_anomaly,
                eccentricity))/(1-eccentricity*cos(eccentric_anomaly))

        num_iterations += 1

    # Error handling
    if num_iterations >= allowed_iterations and abs(
            eccentric_anomaly_iter - eccentric_anomaly) >= tolerance:
        # Did not converge
        raise AbsoluteStateException(
            'convert_anomaly_mean_to_eccentric did not converge.')

    return eccentric_anomaly


def convert_anomaly_eccentric_to_true(
        eccentric_anomaly: float, eccentricity: float) -> float:
    '''Convert the eccentric anomaly to true anomaly

    Args:
        eccentric_anomaly (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        true anomaly (`float`)

    Source:
        Ref. 1 page 215, Eq. 4-14
    '''
    return 2 * atan(
        sqrt((1+eccentricity)/(1-eccentricity)) * tan(eccentric_anomaly/2)
    )


def convert_anomaly_true_to_eccentric(
        true_anomaly: float, eccentricity: float) -> float:
    '''Convert the true anomaly to eccentric anomaly

    Args:
        true_anomaly (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        eccentric anomaly (`float`)

    Source:
        Ref. 1 page 215, Eq. 4-14
    '''
    return 2 * atan(
        sqrt((1-eccentricity)/(1+eccentricity)) * tan(true_anomaly/2)
    )


def convert_anomaly_eccentric_to_mean(
        eccentric_anomaly: float, eccentricity: float) -> float:
    '''Convert the eccentric anomaly to mean anomaly

    Args:
        eccentric_anomaly (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        mean anomaly (`float`)

    Source:
        Ref. 1 page 211, Eq. 4-6
    '''
    return eccentric_anomaly - eccentricity * sin(eccentric_anomaly)


def convert_anomaly_mean_to_true(
        mean_anomaly: float, eccentricity: float) -> float:
    '''TODO

    Args:
        mean_anomaly (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        TODO
    '''
    return


def convert_anomaly_true_to_mean(
        true_anomaly: float, eccentricity: float) -> float:
    '''TODO

    Args:
        true_anomaly (`float`): semi-major axis of the orbit [m]
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
