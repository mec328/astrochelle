# test_epoch
# ------------------------------------------------------------------------------

# Python imports
import pytest 

# Astrochelle imports
from astrochelle.utils.epoch import *

def test_epoch_initialization():
    # Pass on ymdhm (no seconds or nano seconds)
    try:
        epoch = Epoch(
            year = 2022,
            month = 7,
            day = 27,
            hours = 12,
            minutes = 5)
    except Exception:
        assert False

    # Pass on ymdhms(ns?)
    try:
        epoch = Epoch(
            year = 2022,
            month = 7,
            day = 27,
            hours = 12,
            minutes = 5,
            seconds = 5,
            nanoseconds = 100)
    except Exception:
        assert False    

    # One or more of year, month, day, hours, minutes not provided on initialization 
    with pytest.raises(Exception):
        epoch = Epoch(year = 2022)