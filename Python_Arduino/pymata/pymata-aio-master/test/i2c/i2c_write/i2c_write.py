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


This file demonstrates using PyMata to read temperature values from a SparkFun Digital Temperature Sensor
Breakout for the TMP102 device - SparkFun part #SEN-11931

The code is adapted from the Adafruit backpack library https://github.com/adafruit/Adafruit-LED-Backpack-Library

It utilizes the bi_color_display_controller which, in turn, utilizes PyFirmata for I2C write control.
"""


# from  examples.i2c.pymata_i2c_write.bicolor_display_controller import BiColorDisplayController


from test.i2c.i2c_write.bicolor_display_controller import BiColorDisplayController

frown = [0x3C, 0x42, 0xA5, 0x91, 0x91, 0xA5, 0x42, 0x3C]
neutral = [0x3C, 0x42, 0x95, 0x91, 0x91, 0x95, 0x42, 0x3C]
smile = [0x3C, 0x42, 0x95, 0xA1, 0xA1, 0x95, 0x42, 0x3C]


# instantiate a controller object
display = BiColorDisplayController(0x70, 0, 7)

# turn off all leds in display
display.clear_display_buffer()

# let's make some faces
display.set_bit_map(frown, display.LED_RED)
display.firmata.sleep(1)
display.clear_display_buffer()
display.set_bit_map(neutral, display.LED_YELLOW)
display.firmata.sleep(1)
display.clear_display_buffer()
display.set_bit_map(smile, display.LED_GREEN)
display.firmata.sleep(1)
display.clear_display_buffer()

# short but sweet demo
display.close()
