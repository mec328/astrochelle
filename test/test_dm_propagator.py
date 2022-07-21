# test_dm_propagator
# ------------------------------------------------------------------------------

# Python imports

# Astrochelle imports
from astrochelle.utils.data_models.dm_propagator import *

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

