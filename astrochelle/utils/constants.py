#!/usr/bin/env python
# ------------------------------------------------------------------------------
# constants
# DESCRIPTION: constants file, boogie woogie woogie!
# AUTHOR: Michelle Chernick
# CREATED: 2022-07-30
# REFERENCES:
#   [1] Vallado, David A. Fundamentals of astrodynamics and applications.
#       First edition.
# ------------------------------------------------------------------------------

##################
# Math constants #
##################

# TODO

#################################
# Calendar and timing constants #
#################################

# Seconds in a day #
SECONDS_IN_DAY = 86400

# Minimum allowed calendar year for UTC to MJD conversion #
YEAR_MIN = -4713  # 4713 BC from Ref. 1, page 67

# Number of days in each calendar month #
DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}  # Definitely had to do the song to get these

# Offset between JD and MJD #
MJD_OFFSET = 2400000.5
