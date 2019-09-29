#!/usr/bin/env python3

"""
Copyright (c) 2015 Alan Yorinks All rights reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU  General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

You should have received a copy of the GNU  General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


"""

# import the API class
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants


# create a PyMata instance
board = PyMata3()

# configure 4 pins for 4 SONAR modules
board.play_tone(9, Constants.TONE_TONE, 2000, 1500)
board.sleep(3)
board.play_tone(9, Constants.TONE_NO_TONE, 2000, 500)

board.shutdown()
