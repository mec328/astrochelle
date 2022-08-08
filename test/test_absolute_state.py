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

    # Eccentric to mean applied to mean to eccentric should
    # return the original value
    mean_anomaly = 2.345
    eccentricity = 0.35
    assert abs(convert_anomaly_eccentric_to_mean(
        eccentric_anomaly=convert_anomaly_mean_to_eccentric(
            mean_anomaly=mean_anomaly,
            eccentricity=eccentricity),
        eccentricity=eccentricity
    ) - mean_anomaly) < 1e-7


def test_convert_anomaly_eccentric_to_true():
    # True to eccentric applied to eccentric to true should
    # return the original value
    eccentric_anomaly = 2.345
    eccentricity = 0.35
    assert abs(convert_anomaly_true_to_eccentric(
        true_anomaly=convert_anomaly_eccentric_to_true(
            eccentric_anomaly=eccentric_anomaly,
            eccentricity=eccentricity),
        eccentricity=eccentricity
    ) - eccentric_anomaly) < 1e-7

    # Circular orbit, eccentric and true should match
    eccentric_anomaly = 1.123
    eccentricity = 1e-7
    assert abs(convert_anomaly_eccentric_to_true(
        eccentric_anomaly=eccentric_anomaly,
        eccentricity=eccentricity) - eccentric_anomaly) < 1e-7


def test_convert_anomaly_true_to_eccentric():
    # Eccentric to true applied to true to eccentric should
    # return the original value
    true_anomaly = 2.345
    eccentricity = 0.35
    assert abs(convert_anomaly_eccentric_to_true(
        eccentric_anomaly=convert_anomaly_true_to_eccentric(
            true_anomaly=true_anomaly,
            eccentricity=eccentricity),
        eccentricity=eccentricity
    ) - true_anomaly) < 1e-7

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

    # Circular orbit, eccentric and mean should match
    eccentric_anomaly = 1.987
    eccentricity = 1e-7
    assert abs(convert_anomaly_eccentric_to_mean(
        eccentric_anomaly=eccentric_anomaly,
        eccentricity=eccentricity) - eccentric_anomaly) < 1e-7

    # Mean to eccentric applied to eccentric to mean should
    # return the original value
    eccentric_anomaly = 2.345
    eccentricity = 0.35
    assert abs(convert_anomaly_mean_to_eccentric(
        mean_anomaly=convert_anomaly_eccentric_to_mean(
            eccentric_anomaly=eccentric_anomaly,
            eccentricity=eccentricity),
        eccentricity=eccentricity
    ) - eccentric_anomaly) < 1e-7


def test_convert_anomaly_mean_to_true():
    # True to mean applied to mean to true should
    # return the original value
    mean_anomaly = .65
    eccentricity = 0.65
    assert abs(convert_anomaly_true_to_mean(
        true_anomaly=convert_anomaly_mean_to_true(
            mean_anomaly=mean_anomaly,
            eccentricity=eccentricity),
        eccentricity=eccentricity
    ) - mean_anomaly) < 1e-7


def test_convert_anomaly_true_to_mean():
    # Mean to true applied to true to mean should
    # return the original value
    true_anomaly = .65
    eccentricity = 0.65
    assert abs(convert_anomaly_mean_to_true(
        mean_anomaly=convert_anomaly_true_to_mean(
            true_anomaly=true_anomaly,
            eccentricity=eccentricity),
        eccentricity=eccentricity
    ) - true_anomaly) < 1e-7


def test_construct_gve_matrix():
    # TODO eccentricity >= 1, ensure exception raised

    # TODO eccentricity <= 0, ensure exception raised

    # TODO regular GVE matrix construction, expected results
    # zeros in the right spots
    pass
