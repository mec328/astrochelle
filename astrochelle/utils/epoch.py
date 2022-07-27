#!/usr/bin/env python
# ------------------------------------------------------------------------------
# epoch
# DESCRIPTION: all things timing
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-26
# ------------------------------------------------------------------------------

# Python imports
import numpy as np

# Astrochelle imports

##################
# Error Handling #
##################
class EpochException(Exception):
    '''Exceptions related to epoch
    '''
    def __init__(
        self, 
        msg: str = "Something went wrong in epoch.py."
        ):

        super().__init__(msg)


#########
# Epoch #
#########
class Epoch():
    def __init__(
        self
        ):
        '''Time-keeping class

        Args:
            TODO

        Attributes:
            TODO
        '''

        # right now i realllllly don't care if this covers everything... i just want a simple representation of the epoch and associated 
        # overwritten math funcs
