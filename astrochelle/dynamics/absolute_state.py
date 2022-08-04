#!/usr/bin/env python
# ------------------------------------------------------------------------------
# absolute_state
# DESCRIPTION: absolute state structure and propagation classes
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-25
# ------------------------------------------------------------------------------

# Python imports
import numpy as np

# Astrochelle imports
from astrochelle.utils.epoch import Epoch
from astrochelle.utils.data_models.dm_propagator import GVEPropagatorConfig

###################
# GVE Propagation #
###################


class GVEPropagator():
    def __init__(self, propagator_config: GVEPropagatorConfig):
        '''Gauss Variational Equation propagation class for 
        Keplerian orbital elements

        Args:
            propagator_config (`GVEPropagatorConfig`): propagator configuration
                see `dm_propagator.py`

        Attributes:
            propagator_config (`GVEPropagatorConfig`): propagator configuration
                see `dm_propagator.py`
            TODO
        '''

        # Set attributes
        self.propagator_config = propagator_config

        # probs just its config data model and then propagation methods
        # themselves, aka step(), accelerations, etc

    def step(self, timestep: float = None, to_epoch: Epoch = None):
        '''Step forward in time

        Args:
            timestep (`float`): propagate state in time by this increment [s]
                or
            to_epoch (`Epoch`): 

        Modifies:
            TODO
        '''
        if timestep is not None:
            print('hi')

        elif to_epoch is not None:
            print('hey')

        return


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
