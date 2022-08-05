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
        eccentricity=eccentricity) - 3.8486971) < 1e-4


def test_convert_anomaly_eccentric_to_true():
    # TODO
    pass


def test_convert_anomaly_true_to_eccentric():
    # TODO
    pass


def test_convert_anomaly_eccentric_to_mean():
    # TODO
    pass


def test_convert_anomaly_mean_to_true():
    # TODO
    pass


def test_convert_anomaly_true_to_mean():
    # TODO
    pass


def test_construct_gve_matrix():
    # TODO
    pass
