#!/usr/bin/env python3


"""
Copyright (c) 2013 Alan Yorinks All rights reserved.
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
This file demonstrates using PyMata to control a stepper motor. It requires the use of the FirmataPlus
Arduino sketch included with this release.

It is based upon the following tutorial: https://learn.adafruit.com/adafruit-arduino-lesson-16-stepper-motors/overview
"""


from pymata_aio.pymata3 import PyMata3


# create a PyMata instance
# ping callback function
def vr(data):
    # print('hello')
    print('version')
    print(data)

# create a PyMata instance
# create a PyMata instance
firmata = PyMata3(2)

# send the arduino a firmata reset
firmata.send_reset()

# configure the stepper to use pins 9.10,11,12 and specify 512 steps per revolution
firmata.stepper_config(180, [8, 9, 10, 11])

# allow time for config to complete
firmata.sleep(.5)


# move motor #0 500 steps forward at a speed of 20
firmata.stepper_step(20, 500)

# firmata.sleep(4)

# move motor #0 500 steps reverse at a speed of 20
# firmata.stepper_step(20, -500)

# close firmata
firmata.shutdown()
