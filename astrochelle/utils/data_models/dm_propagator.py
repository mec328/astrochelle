#!/usr/bin/env python
# ------------------------------------------------------------------------------
# dm_propagator
# DESCRIPTION: Data models used in the propagator
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-21
# ------------------------------------------------------------------------------

# Python imports
from pydantic import BaseModel, Field, ValidationError, validator

# Astrochelle imports

#####################
# PROPAGATOR CONFIG #
#####################
class GVEPropagatorConfig(BaseModel):
    timestep: float = Field(10, description = "time step for simulation [s]")
    gravity_degree: int = Field(60, description = "spherical harmonic degree")
    gravity_order: int = Field(60, description = "spherical harmonic order")

    @validator('gravity_order')
    def gravity_order_must_be_less_than_degree(cls, order):
        if order > cls.gravity_degree:
            raise ValueError('Gravity order cannot be greater than degree.')
        return order
