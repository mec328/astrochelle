#!/usr/bin/env python
# ------------------------------------------------------------------------------
# dm_propagator
# DESCRIPTION: Data models used in the propagator
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-21
# ------------------------------------------------------------------------------

# Python imports
from pydantic import BaseModel, Field, validator

# Astrochelle imports

#####################
# PROPAGATOR CONFIG #
#####################


class GVEPropagatorConfig(BaseModel):
    timestep: float = Field(10, description="time step for simulation [s]")
    gravity_degree: int = Field(60, description="spherical harmonic degree")
    gravity_order: int = Field(60, description="spherical harmonic order")
    flag_atmospheric_drag: bool = Field(True,
                                        description="flag include drag")
    model_atmospheric_drag: str = Field('nrlmsise00',
                                        description="drag model to use")
    flag_solar_radiation_pressure: bool = Field(True,
                                                description="flag include SRP")
    model_solar_radiation_pressure: str = Field('flat_plate',
                                                description="SRP model to use")
    model_third_body: list = Field(['sun', 'moon'],
                                   description="planetary bodies to include")
    flag_relativity: bool = Field(True,
                                  description="include relativistic effects")

    @validator('gravity_order')
    def gravity_order_must_be_less_than_degree(cls, order, values):
        if order > values['gravity_degree']:
            raise ValueError('Gravity order cannot be greater than degree.')
        return order

    @validator('model_atmospheric_drag')
    def model_must_exist_drag(cls, model, values, field):
        # TODO might add harrispriester but it sux so probs not
        if model not in ['nrlmsise00']:
            raise ValueError(f"Model {model} is not valid for {field.name}.")

    @validator('model_solar_radiation_pressure')
    def model_must_exist_srp(cls, model, values, field):
        if model not in ['flat_plate', 'conical']:
            raise ValueError(f"Model {model} is not valid for {field.name}.")

    @validator('model_third_body')
    def model_must_exist_third_body(cls, model):
        allowed_bodies = ['sun', 'moon']
        if not all([body in allowed_bodies for body in model]):
            raise ValueError(f"One of the bodies in {model} is not valid.")
