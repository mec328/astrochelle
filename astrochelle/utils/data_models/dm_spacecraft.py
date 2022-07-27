#!/usr/bin/env python
# ------------------------------------------------------------------------------
# dm_spacecraft
# DESCRIPTION: Spacecraft parameter model
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-25
# ------------------------------------------------------------------------------

# Python imports
from pydantic import BaseModel, Field, validator

# Astrochelle imports

#####################
# SPACECRAFT CONFIG #
#####################


class SpacecraftConfig(BaseModel):
    # TODO, have this generate automatically on initialization
    id: int = Field(0, description="unique spacecraft identifier")
    mass: float = Field(100, description="spacecraft mass [kg]")
    coefficient_drag: float = Field(1, description="coefficient of drag")
    coefficient_srp: float = Field(1, description="coefficient of SRP")
    effective_area_drag: float = Field(1,
                                       description="effective drag area [m^2]")
    effective_area_srp: float = Field(1,
                                      description="effective SRP area [m^2]")

    @validator('mass', 'coefficient_drag', 'coefficient_srp',
               'effective_area_drag', 'effective_area_srp')
    @classmethod
    def fields_nonnegative(cls, field_val, values, field, config):
        if field_val < 0:
            raise ValueError(f"Ma''am, {field.name} must be non-negative.")
    # TODO need more validators
