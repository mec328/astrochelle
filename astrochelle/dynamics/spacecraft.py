#!/usr/bin/env python
# ------------------------------------------------------------------------------
# spacecraft
# DESCRIPTION: spacecraft class and methods!
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-26
# ------------------------------------------------------------------------------

# Python imports
import numpy as np

# Astrochelle imports
from astrochelle.utils.data_models.dm_spacecraft import *

##################
# Error Handling #
##################
class SpacecraftException(Exception):
    '''Exceptions related to spacecraft
    '''
    def __init__(
        self, 
        msg: str = "Something went wrong in spacecraft.py."
        ):

        super().__init__(msg)


##############
# Spacecraft #
##############
class Spacecraft():
    def __init__(
        self,
        initial_state: np.array,
        initial_state_type: str
        ):
        '''Class representing a spacecraft

        Args:
            initial_epoch (`Epoch`): aw shiet TODO
            initial_state (`np.array`): 6 dof initial state of spacecraft
            initial_state_type (`str`): type of the initial state ('koe','eci', TODO more to come when i write conversions)

        Attributes:
            epoch (`Epoch`): aw shiet TODO
            state (`np.array`): 6 dof current state of spacecraft
            state_type (`str`): type of the state ('koe','eci', TODO more to come when i write conversions)
        '''

        # Check size of initial state
        if not initial_state.size == 6:
            raise SpacecraftException(msg = f"Provided initial state is size {initial_state.size}. Initial state must be size 6.")

