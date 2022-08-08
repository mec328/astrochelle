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

    if mean_anomaly > -pi and mean_anomaly < 0 or mean_anomaly > pi:
        eccentric_anomaly = mean_anomaly - eccentricity
    else:
        eccentric_anomaly = mean_anomaly + eccentricity

    # Initialize error value using the expression in Algorithm 25 in Ref. 1
    # (page 232)
    eccentric_anomaly_iter = eccentric_anomaly + \
        (mean_anomaly - convert_anomaly_eccentric_to_mean(
            eccentric_anomaly,
            eccentricity))/(1-eccentricity*cos(eccentric_anomaly))

    num_iterations = 0
    while num_iterations < allowed_iterations and abs(
            eccentric_anomaly_iter - eccentric_anomaly) >= tolerance:
        # Save last iteration's eccentric anomaly value
        eccentric_anomaly = eccentric_anomaly_iter

        # Re-calculate eccentric anomaly using same Algorithm
        eccentric_anomaly_iter = eccentric_anomaly + \
            (mean_anomaly - convert_anomaly_eccentric_to_mean(
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
    '''Convert the mean anomaly to true anomaly

    Args:
        mean_anomaly (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        true anomaly (`float`)
    '''
    return convert_anomaly_eccentric_to_true(
        eccentric_anomaly=convert_anomaly_mean_to_eccentric(
            mean_anomaly=mean_anomaly, eccentricity=eccentricity),
        eccentricity=eccentricity)


def convert_anomaly_true_to_mean(
        true_anomaly: float, eccentricity: float) -> float:
    '''Convert the true anomaly to mean anomaly

    Args:
        true_anomaly (`float`): semi-major axis of the orbit [m]
        eccentricity (`float`): eccentricity of the orbit

    Returns:
        mean anomaly (`float`)
    '''
    return convert_anomaly_eccentric_to_mean(
        eccentric_anomaly=convert_anomaly_true_to_eccentric(
            true_anomaly=true_anomaly, eccentricity=eccentricity),
        eccentricity=eccentricity)


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
    w = koe[4]

    # Check eccentricity to ensure no divide by zero errors
    if e <= 0 or e >= 1:
        raise AbsoluteStateException(
            f'Cannot construct GVE matrix with ecc <= 0 or >=1. Ecc = {e}')

    # Compute mean motion
    mean_motion = calculate_mean_motion(semimajor_axis=a)

    # Convert mean anomaly to true
    nu = convert_anomaly_mean_to_true(mean_anomaly=koe[5], eccentricity=e)

    # Compute relevant constants TODO write down what each of these are
    eta = sqrt(1-e**2)
    p = a*eta**2  # Semi-latus rectum
    h = sqrt(p * GM_EARTH)
    r = p/(1+e*cos(nu))

    # Fill in the matrix
    gve_matrix[0, 0] = 2/h * a**2 * e*sin(nu)
    gve_matrix[0, 1] = 2/(h*r) * a**2 * p

    gve_matrix[1, 0] = p/h * sin(nu)
    gve_matrix[1, 1] = 1/h * (((p+r)*cos(nu))+(r*e))

    gve_matrix[2, 2] = r*cos(nu+w)/h

    gve_matrix[3, 2] = r/(h*sin(i)) * sin(nu+w)

    gve_matrix[4, 0] = -p/(h*e) * cos(nu)
    gve_matrix[4, 1] = (p+r)*sin(nu)/(h*e)
    gve_matrix[4, 2] = -r*sin(nu+w)*cos(i)/(h*sin(i))

    gve_matrix[5, 0] = ((-2*e)+cos(nu)+(e*cos(nu)*cos(nu))) * \
        eta**2/(e*(1+(e*cos(nu)))*mean_motion*a)
    gve_matrix[5, 1] = ((e**2 - 1)*((e*cos(nu))+2)*sin(nu)) / \
        (e*(1+(e*cos(nu)))*mean_motion*a)

    return gve_matrix
