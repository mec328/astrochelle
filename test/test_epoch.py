# test_epoch
# ------------------------------------------------------------------------------

# Python imports
import pytest

# Astrochelle imports
from astrochelle.utils.epoch import *


def test_epoch_initialization():
    # Pass on ymdhm (no seconds)
    try:
        epoch = Epoch(
            year=2022,
            month=7,
            day=27,
            hours=12,
            minutes=5)
    except Exception:
        assert False

    # Pass on ymdhms
    try:
        epoch = Epoch(
            year=2022,
            month=7,
            day=27,
            hours=12,
            minutes=5,
            seconds=5)
    except Exception:
        assert False

    # One or more of year, month, day, hours, minutes not provided on
    # initialization
    with pytest.raises(Exception):
        epoch = Epoch(year=2022)

    # TODO MORE HERE


def test_check_validity_date():
    # Defaults
    year = 2022
    month = 7
    day = 27
    hours = 12
    minutes = 5
    seconds = 5

    # TODO pass

    # Year not valid, should return False
    flag_valid, _ = check_validity_date(
        year=-4800, month=month, day=day, hours=hours,
        minutes=minutes, seconds=seconds
    )

    assert flag_valid == False

    # Month not valid, should return False
    flag_valid, _ = check_validity_date(
        year=year, month=13, day=day, hours=hours,
        minutes=minutes, seconds=seconds
    )

    assert flag_valid == False

    # Day not in provided month, should return False
    flag_valid, _ = check_validity_date(
        year=year, month=13, day=day, hours=hours,
        minutes=minutes, seconds=seconds
    )

    assert flag_valid == False

    # It's not a leap year but month is Feb and day is 29, should return False
    flag_valid, _ = check_validity_date(
        year=2021, month=2, day=29, hours=hours,
        minutes=minutes, seconds=seconds
    )

    assert flag_valid == False

    # It is a leap year and month is February and day is 29, should return True
    flag_valid, _ = check_validity_date(
        year=2020, month=2, day=29, hours=hours,
        minutes=minutes, seconds=seconds
    )

    assert flag_valid

    # Negative hours
    flag_valid, _ = check_validity_date(
        year=year, month=month, day=day, hours=-10,
        minutes=minutes, seconds=seconds
    )

    assert flag_valid == False

    # Negative minutes
    flag_valid, _ = check_validity_date(
        year=year, month=month, day=day, hours=hours,
        minutes=-5, seconds=seconds
    )

    assert flag_valid == False

    # MORE HERE TODO


def test_check_leap_year():
    # Is leap year
    assert check_leap_year(year=2020)

    # Is not divisible by 4, not leap year
    assert not check_leap_year(year=2021)

    # Is divisible by 4 but also by 100 and not by 400, not leap year
    assert not check_leap_year(year=1900)
