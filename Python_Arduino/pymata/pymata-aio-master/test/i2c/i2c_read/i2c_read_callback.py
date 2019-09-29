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


This file demonstrates using PyMata to read temperature values from a SparkFun Digital Temperature Sensor
Breakout for the TMP102 device - SparkFun part #SEN-11931

The code is based on a bildr article: http://bildr.org/2011/01/tmp102-arduino/
"""

# import the API class

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants


def my_callback(data):
    if data:
        # do some calculations on the raw data returned
        # reconstruct integer out of data

        raw_temperature = (data[4] << 8 | data[6]) >> 4

        celsius = raw_temperature * 0.0625
        print(celsius)
        fahrenheit = (1.8 * celsius) + 32
        print(fahrenheit)


# create a PyMata instance
board = PyMata3(2)

# configure firmata for i2c on an UNO
board.i2c_config(0)

# read i2c device at address 0x48, with no register specified. Expect 2 bytes to be returned
# and the operation is a single shot read

# reading for 5 seconds
board.i2c_read_request(0x48, 0, 2, Constants.I2C_READ_CONTINUOUSLY, my_callback)
board.sleep(5)
board.i2c_read_request(0x48, 0, 2, Constants.I2C_STOP_READING, my_callback)

board.sleep(1)
board.shutdown()
