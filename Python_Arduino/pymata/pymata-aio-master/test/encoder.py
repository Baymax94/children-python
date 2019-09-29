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


# ping callback function
def encoder_val(data):
    print(str(data[2]) + ' centimeters')

# create a PyMata instance
board = PyMata3(2)

board.encoder_config(15, 14)

while True:
    board.sleep(.001)
    value = board.encoder_read(15)
    print(value)

# board.sleep(.1)
board.shutdown()
