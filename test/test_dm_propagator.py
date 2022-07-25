# test_dm_propagator
# ------------------------------------------------------------------------------

# Python imports
import pytest

# Astrochelle imports
from astrochelle.utils.data_models.dm_propagator import *

def test_gve_propagator_config_pass():
    # TODO
    pass

def test_gve_propagator_config_fail():
    # Defaults
    timestep = 10 # 10 seconds
    gravity_degree = 60
    gravity_order = 60
    flag_atmospheric_drag = True
    model_atmospheric_drag = 'nrlmsise00'

    # Order greater than degree
    with pytest.raises(Exception):
        propagator_config = GVEPropagatorConfig(
            gravity_order = 70
            )


