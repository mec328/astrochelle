# test_dm_propagator
# ------------------------------------------------------------------------------

# Python imports
import pytest

# Astrochelle imports
from astrochelle.utils.data_models.dm_spacecraft import *

def test_spacecraft_config_pass():
    # TODO
    pass

def test_spacecraft_config_fail():
    # Defaults
    mass = 100
    drag_coef = 1 
    srp_coef = 1
    drag_area = 1
    srp_area = 1

    # TODO needs a loop

    # Negative mass should raise exception
    with pytest.raises(Exception):
        spacecraft_config = SpacecraftConfig(
            mass = -100,
            coefficient_drag = drag_coef,
            coefficient_srp = srp_coef,
            effective_area_drag = drag_area,
            effective_area_srp = srp_area
            )


