# test_absolute_state
# References:
#   [1] Vallado, David A. Fundamentals of astrodynamics and applications.
#       First edition.
# ------------------------------------------------------------------------------

# Python imports
from math import pi
import pytest

# Astrochelle imports
from astrochelle.utils.absolute_state import *


def test_convert_anomaly_mean_to_eccentric():
    # From Example 4.1 on page 233 in Ref. 1
    mean_anomaly = 235.4 * pi / 180
    eccentricity = 0.4

    assert abs(convert_anomaly_mean_to_eccentric(
        mean_anomaly=mean_anomaly,
        eccentricity=eccentricity) - 3.8486617) < 1e-7

    # Circular orbit, mean and eccentric should match
    eccentricity = 1e-7
    assert abs(convert_anomaly_mean_to_eccentric(
        mean_anomaly=mean_anomaly,
        eccentricity=eccentricity) - mean_anomaly) < 1e-7


def test_convert_anomaly_eccentric_to_true():
    # TODO
    pass

    # Circular orbit, eccentric and true should match
    eccentric_anomaly = 1.123
    eccentricity = 1e-7
    assert abs(convert_anomaly_eccentric_to_true(
        eccentric_anomaly=eccentric_anomaly,
        eccentricity=eccentricity) - eccentric_anomaly) < 1e-7


def test_convert_anomaly_true_to_eccentric():
    # TODO
    pass

    # Circular orbit, eccentric and true should match
    true_anomaly = 1.567
    eccentricity = 1e-7
    assert abs(convert_anomaly_true_to_eccentric(
        true_anomaly=true_anomaly,
        eccentricity=eccentricity) - true_anomaly) < 1e-7


def test_convert_anomaly_eccentric_to_mean():
    # From (reverse of) Example 4.1 on page 233 in Ref. 1
    eccentric_anomaly = 3.8486617
    eccentricity = 0.4

    assert abs(convert_anomaly_eccentric_to_mean(
        eccentric_anomaly=eccentric_anomaly,
        eccentricity=eccentricity) - 235.4 * pi / 180) < 1e-7

    # TODO more


def test_convert_anomaly_mean_to_true():
    # TODO
    pass


def test_convert_anomaly_true_to_mean():
    # TODO
    pass


def test_construct_gve_matrix():
    # TODO
    pass
