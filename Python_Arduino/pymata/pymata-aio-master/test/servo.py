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

You should have received a copy of the GNU General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

"""
This example illustrates manipulating a servo motor.
"""

from pymata_aio.pymata3 import PyMata3

# instantiate PyMata with a 2 second start up delay to allow an Uno to complete its reset
board = PyMata3(2)

SERVO_MOTOR = 5  # servo attached to this pin

# configure the servo
board.servo_config(SERVO_MOTOR)

for x in range(0, 3):
    # move the servo to 20 degrees
    board.analog_write(SERVO_MOTOR, 20)
    board.sleep(1)

    # move the servo to 100 degrees
    board.analog_write(SERVO_MOTOR, 100)
    board.sleep(1)

    # move the servo to 20 degrees
    board.analog_write(SERVO_MOTOR, 20)

# close the interface down cleanly
board.shutdown()
