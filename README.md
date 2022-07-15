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
Note: `astrochelle` was developed using Python 3.6. I have not (yet) tested it in other releases.

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