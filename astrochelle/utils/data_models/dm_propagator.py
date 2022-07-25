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
    flag_atmospheric_drag: bool = Field(True, description = "flag to include drag")
    model_atmospheric_drag: str = Field('nrlmsise00', description = "drag model to use")

    @validator('gravity_order')
    def gravity_order_must_be_less_than_degree(cls, order, values, field, config):
        if order > values['gravity_degree']:
            raise ValueError('Gravity order cannot be greater than degree.')
        return order

    @validator('model_atmospheric_drag')
    def model_must_exist(cls, model, values, field, config):
        if not model in ['nrlmsise00']: # TODO might add harrispriester but it sux so probs not
            raise ValueError(f"Model {model} is not valid for {field.name}.")
