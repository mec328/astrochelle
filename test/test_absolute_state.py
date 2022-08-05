# test_absolute_state
#
# References:
# ------------------------------------------------------------------------------

# Python imports
import pytest
from math import pi

# Astrochelle imports
from astrochelle.dynamics.absolute_state import *


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
    # TODO
    pass


def test_step():
    # Provide timestep and acceleration
    propagator = propagator_example()
    propagator.step(timestep=5, acceleration=np.array([.5, .6, .7]))

    # Provide timestep, no acceleration (so it calculates it internally) TODO

    # No timestep, provide acceleration
    #   (should use default timestep)

    # No timestep, no acceleration
    # (so it uses default timestep and calculates acceleration internally) TODO
    pass


def test_step_to_timestep():
    # Raise error if timestep is negative

    # TODO more
    pass


def test_step_to_to_epoch():
    # Raise error if provided epoch is behind current epoch

    # TODO more
    pass
