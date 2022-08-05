#!/usr/bin/env python
# ------------------------------------------------------------------------------
# state_propagation
# DESCRIPTION: absolute state propagation classes
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-25
# TODO:
#   Add propagation method to config, rather than just defaulting to rk45
# ------------------------------------------------------------------------------

# Python imports
import numpy as np
from copy import deepcopy
from scipy import integrate

# Astrochelle imports
from astrochelle.utils.absolute_state import calculate_mean_motion
from astrochelle.utils.epoch import Epoch
from astrochelle.utils.data_models.dm_propagator import GVEPropagatorConfig

##################
# Error Handling #
##################


class StatePropagationException(Exception):
    '''Exceptions related to absolute state
    '''

    def __init__(
        self,
        msg: str = "Something went wrong in absolute_state.py."
    ):

        super().__init__(msg)

###################
# GVE Propagation #
###################


class GVEPropagator():
    def __init__(self,
                 propagator_config: GVEPropagatorConfig,
                 initial_epoch: Epoch,
                 initial_state: np.array
                 ):
        '''Gauss Variational Equation propagation class for
        Keplerian orbital elements

        Args:
            propagator_config (`GVEPropagatorConfig`): propagator configuration
                see `dm_propagator.py`
            initial_epoch (`Epoch`): epoch at which to start propagation
            initial_state (`np.array`): 6 dof initial state of spacecraft
            TODO

        Attributes:
            propagator_config (`GVEPropagatorConfig`): propagator configuration
                see `dm_propagator.py`
            epoch (`Epoch`): current epoch
            propagator_time (`float`): time since initial epoch [s]
            state (`np.array`): current state (assumed KOE TODO)
            TODO
        '''

        # Set attributes
        self.propagator_config = propagator_config
        self.epoch = deepcopy(initial_epoch)
        self.propagator_time = 0
        self.state = initial_state

        # TODO probs just its config data model and then propagation methods
        # themselves, aka step(), accelerations, etc

    def step(self, timestep: float = None):
        '''Step forward in time

        Args:
            timestep (`float`): propagate state in time by this increment [s] 
                (optional, will use default if None)

        Modifies:
            epoch
            state
        '''
        # If no timestep is provided, just step by default
        # If timestep is provided, step by that amount (note this can cause
        # issues if timestep is too large!!)
        if timestep is None:
            timestep = self.timestep

        # Integrate
        self.state = integrate.rk45(
            fun=self.state_derivative,
            t0=self.propagator_time,
            y0=self.state,
            t_bound=self.propagator_time+timestep
        )

        # Increment time
        self.epoch += timestep
        self.propagator_time += timestep

    def step_to(self, timestep: float = None, to_epoch: Epoch = None):
        '''Step forward in time

        Args:
            timestep (`float`): propagate state in time by this increment [s]
                or
            to_epoch (`Epoch`): epoch to propagate to

        Modifies:
            TODO

        Returns:
            TODO

        Notes:
            if no timestep or epoch is provided, step forward by default
                timestep (aka identical to step function)
        '''
        if timestep is not None:
            # Step forward by provided timestep by increments of the
            # default time step

            # Check that the timestep is not negative
            if timestep < 0:
                raise AbsoluteStateException(
                    'Cannot propagate backwards. Quitting.')

            return

        elif to_epoch is not None:
            # Step forward to a given Epoch by increments of the
            # default time step

            # Check that the epoch is not in the past
            if to_epoch - self.epoch < 0:
                raise AbsoluteStateException(
                    'Cannot propagate backwards. Quitting.')
            return

        else:
            # No input provided, use default
            # TODO call step
            self.step()
            return

    def state_derivative(self, timestep: float, state: np.array) -> np.array:
        '''State derivative for KOE state for use in integration

        Args:
            timestep (`float`): TODO
            state (`np.array`): TODO

        Modifies:
            TODO

        Returns:
            TODO
        '''
        # Calculate RTN acceleration
        acceleration = self.calculate_acceleration()

        # See lines 66-202 in old gve code

        # Compute GVE matrix

        # Apply to acceleration to convert from RTN to OE
        state_derivative = np.zeros(6)

        # Add Keplerian motion
        mean_motion = calculate_mean_motion(semimajor_axis=self.state[0])
        state_derivative += np.array([0, 0, 0, 0, 0, mean_motion])

        return state_derivative

    def calculate_acceleration(self) -> np.array:
        '''Calculate acceleration at current time in RTN 
        for use in integration

        Args:
            TODO

        Modifies:
            TODO

        Returns:
            acceleration (`np.array`): 3 dimensional acceleration in RTN
        '''
        # TODO
        return np.zeros(3)


def propagate_formation(spacecraft: list, propagator):
    '''TODO this is where we'd load in list of spacecraft and the propagator

    Args:
       spacecraft (`list`): list of `Spacecraft` objects
       propagator: initialized propagator object of choice (currently only GVE)

    Returns:
        TODO
    '''
    # For each spacecraft in the list
    # Get its initial state and config params, propagate
    # Update the spacecraft state in the object, and output all the data

    return
