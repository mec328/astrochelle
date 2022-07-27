# test_epoch
# ------------------------------------------------------------------------------

# Python imports
import pytest 

# Astrochelle imports
from astrochelle.utils.epoch import *

def test_epoch_initialization():
    # TODO pass on ymdhms

    # One or more of year, month, day, hours, minutes not provided on initialization 
    with pytest.raises(Exception):
        epoch = Epoch(year = 2022)