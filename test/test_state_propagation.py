# test_state_propagation
#
# References:
# ------------------------------------------------------------------------------

# Python imports
import pytest
from math import pi, sqrt

# Astrochelle imports
from astrochelle.utils.constants import GM_EARTH
from astrochelle.dynamics.state_propagation import *


def propagator_example() -> GVEPropagator:
    # Example propagator for use in tests
    # Default configuration paramteres
    timestep = 10  # 10 seconds
    gravity_degree = 60
    gravity_order = 60
    flag_atmospheric_drag = True
    model_atmospheric_drag = 'nrlmsise00'
    flag_srp = True
    model_srp = 'conical'
    model_third_body = ['sun', 'moon']
    flag_relativity = True

    initial_epoch = Epoch(
        year=2022,
        month=8,
        day=3,
        hours=17,
        minutes=19)

    # Here's an arbitrary near-circular orbit lol
    initial_state = np.array([6878e3, 1e-4, pi/3, pi/4, pi/5, 0])

    propagator_config = GVEPropagatorConfig(
        timestep=timestep,
        gravity_degree=gravity_degree,
        gravity_order=gravity_order,
        flag_atmospheric_drag=flag_atmospheric_drag,
        model_atmospheric_drag=model_atmospheric_drag,
        flag_solar_radiation_pressure=flag_srp,
        model_solar_radiation_pressure=model_srp,
        model_third_body=model_third_body,
        flag_relativity=flag_relativity
    )

    propagator = GVEPropagator(
        propagator_config=propagator_config,
        initial_epoch=initial_epoch,
        initial_state=initial_state
    )

    return propagator


def test_calculate_acceleration():
    # If no perturbations are included, acceleration should be zero
    propagator = propagator_example()
    propagator.propagator_config.gravity_degree = 0
    propagator.propagator_config.gravity_order = 0
    propagator.propagator_config.flag_atmospheric_drag = False
    propagator.propagator_config.flag_solar_radiation_pressure = False
    propagator.propagator_config.model_third_body = []
    propagator.propagator_config.flag_relativity = False

    assert np.all([val == 0 for val in propagator.calculate_acceleration()])

    # TODO
    pass


def test_state_derivative():
    # If no perturbations are included, state derivative should just include
    # the mean motion
    propagator = propagator_example()
    propagator.propagator_config.gravity_degree = 0
    propagator.propagator_config.gravity_order = 0
    propagator.propagator_config.flag_atmospheric_drag = False
    propagator.propagator_config.flag_solar_radiation_pressure = False
    propagator.propagator_config.model_third_body = []
    propagator.propagator_config.flag_relativity = False

    state_derivative = propagator.state_derivative(
        timestep=propagator.propagator_config.timestep,
        state=propagator.state)

    # First 5 entries should be zeros
    assert np.all(val == 0 for val in state_derivative[:5])

    # Last entry should be mean motion
    mean_motion = sqrt(GM_EARTH/propagator.state[0]**3)
    assert state_derivative[5] == mean_motion

    # TODO
    pass


def test_step():
    # TODO

    # Provide timestep

    # No timestep
    pass


def test_step_to_timestep():
    # Raise error if timestep is negative

    # TODO more
    pass


def test_step_to_to_epoch():
    # Raise error if provided epoch is behind current epoch

    # TODO more
    pass
