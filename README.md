# astrochelle
Hello! This is under construction :)
All documentation will live [here](https://nervous-warrior-341.notion.site/Astrochelle-Documentation-bf84b08ebde04c67a72b2277abccf38a).

## What is this?
*Hopefully* this will be a stable, helpful, open source of validated guidance, navigation, dynamics, and control code functionality, all written in Python.

## Why should we trust you, Michelle?
I've got good credentials! --> [my linkedin](https://www.linkedin.com/in/michelle-chernick/)

I'm a big believer in code validation. All functionality in this repo will be validated in the following ways:
1) *Unit testing*: Functions and class methods will be "small" (simplified and testable). All possible code paths will be tested to ensure that they provide expected, deterministic results and don't catastrophically break.
2) *Simulation testing*: For functions that require timing and propagation, I will include example usage and expected results. 
3) *Validation against existing truth data*: Wherever possible, functionality will be validated against truth data sources such as STK, GMAT, NASA data, etc.

## Can I request features?
Yeah, eventually!

## Authors
**Michelle Chernick** - it me, pushing directly to main

# Installation
If you want to use `astrochelle` as a package, follow the instructions below. 
Note: `astrochelle` was developed using Python 3.6, but the pipeline tests it from 3.6 to 3.10.

## Mac
1. Run 
```
pip3 install -e .
```
from the root directory.

2. Install the requirements via the command
```
pip3 install -r requirements.txt
```

# Repo Structure
The `astrochelle` repo is organized into the following folders:

## astrochelle
Dis dat main shit.

### control
TODO fill in later
### dynamics
TODO fill in later
- propagation
- etc
### utils
TODO fill in later
- absolute state
- relative state
- math
- etc
#### data_models
This folder contains configuration and state files for use within the module. For example, the propagator classes in `dynamics/propagation` are initialized with the `GVEPropagatorConfig` data model. (Why data models? Because they can inherently include validators to ensure that the user isn't setting trash variables.)

## examples
The `examples` folder contains more detailed examples demonstrating code usage. TODO details on running examples

## test
The `test` folder contains unit tests. TODO details on running unit tests, details on pipeline