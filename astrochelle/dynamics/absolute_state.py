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
from astrochelle.utils.data_models.dm_propagator import GVEPropagatorConfig

###################
# GVE Propagation #
###################


class GVEPropagator():
    def __init__(propagator_config: GVEPropagatorConfig):
        '''Gauss Variational Equation propagation class for 
        Keplerian orbital elements

        Args:
            propagator_config (`GVEPropagatorConfig`): propagator configuration
                see `dm_propagator.py`

        Attributes:
            TODO
        '''

        # probs just its config data model and then propagation methods
        # themselves


def propagate_formation(spacecraft: list):
    '''TODO this is where we'd load in list of spacecraft and the propagator

    Args:
       spacecraft (`list`): list of `Spacecraft` objects

    Returns:
        TODO
    '''
    # For each spacecraft in the list
    # Get its initial state and config params, initialize propagator

    return
