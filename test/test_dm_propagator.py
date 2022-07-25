# test_dm_propagator
# ------------------------------------------------------------------------------

# Python imports
import pytest

# Astrochelle imports
from astrochelle.utils.data_models.dm_propagator import *

def test_gve_propagator_config_pass():
    # Defaults
    timestep = 10 # 10 seconds
    gravity_degree = 60
    gravity_order = 60
    flag_atmospheric_drag = True
    model_atmospheric_drag = 'nrlmsise00'
    flag_srp = True
    model_srp = 'conical'
    model_third_body = ['sun', 'moon']
    flag_relativity = True

    try:
        propagator_config = GVEPropagatorConfig(
            timestep = timestep,
            gravity_degree = gravity_degree,
            gravity_order = gravity_order,
            flag_atmospheric_drag = flag_atmospheric_drag,
            model_atmospheric_drag = model_atmospheric_drag,
            flag_solar_radiation_pressure = flag_srp,
            model_solar_radiation_pressure = model_srp,
            model_third_body = model_third_body,
            flag_relativity = flag_relativity
            )
    except Exception:
        assert False

def test_gve_propagator_config_fail():
    # Order greater than degree
    with pytest.raises(Exception):
        propagator_config = GVEPropagatorConfig(
            gravity_order = 70
            )

    # Bad drag model
    with pytest.raises(Exception):
        propagator_config = GVEPropagatorConfig(
            model_atmospheric_drag = 'cats'
            )

    # Bad SRP model
    with pytest.raises(Exception):
        propagator_config = GVEPropagatorConfig(
            model_solar_radiation_pressure = 'meow'
            )

    # Bad third body model
    with pytest.raises(Exception):
        propagator_config = GVEPropagatorConfig(
            model_third_body = ['pluto']
            )

    with pytest.raises(Exception):
        propagator_config = GVEPropagatorConfig(
            model_third_body = ['sun','pluto']
            )


