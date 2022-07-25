#!/usr/bin/env python
# ------------------------------------------------------------------------------
# dm_propagator
# DESCRIPTION: Data models used in the propagator
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-21
# ------------------------------------------------------------------------------

# Python imports
from pydantic import BaseModel, Field

# Astrochelle imports

#####################
# PROPAGATOR CONFIG #
#####################
class PropagatorConfig(BaseModel):
	id: int = Field(0, description = "hello")

class PropagatorState(BaseModel):
	id: int = Field(0, description = "hello")
