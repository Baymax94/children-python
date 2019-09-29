__author__ = 'Copyright (c) 2013 Alan Yorinks All rights reserved.'

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


This file provides a class used in conjunction with PyMata to control an Adafruit
Bicolor LED Square Pixel Matrix with I2C Backpack model 902

The code is adapted from the Adafruit backpack library https://github.com/adafruit/Adafruit-LED-Backpack-Library

"""

from pymata_aio.pymata3 import PyMata3


class BiColorDisplayController:
    # display blink control values

    board_address = 0  # i2c address
    blink_rate = 0  # blink rate
    brightness = 0  # brightness

    # blink rate defines
    HT16K33_BLINK_CMD = 0x80
    HT16K33_BLINK_DISPLAYON = 0x01
    HT16K33_BLINK_OFF = 0
    HT16K33_BLINK_2HZ = 1
    HT16K33_BLINK_1HZ = 2
    HT16K33_BLINK_HALFHZ = 3

    # oscillator control values
    OSCILLATOR_ON = 0x21
    OSCILLATOR_OFF = 0x20

    # led color selectors
    LED_OFF = 0
    LED_RED = 1
    LED_YELLOW = 2
    LED_GREEN = 3

    # brightness
    MAX_BRIGHTNESS = 15

    # the display buffer
    # This is a 8x8 matrix that stores pixel data for the display
    # Even rows store the green pixel data and odd rows store the red pixel data.
    #
    # A physical row on the device is controlled by a row pair (ie 0,1 and 2,3, etc) for the 2 colors.
    #
    # To output yellow the red and green information for the rows will be set high.
    #

    # create an 8x8 buffer
    display_buffer = [[0 for x in range(8)] for y in range(8)]

    def __init__(self, address, blink_rate, brightness):

        # create an instance of PyMata - we are using an Arduino UNO
        """

        @param address: I2C address of the device
        @param blink_rate: desired blink rate
        @param brightness: brightness level for the display
        """

        # create a PyMata instance
        self.firmata = PyMata3()

        self.board_address = address
        self.blink_rate = blink_rate
        self.brightness = brightness
        self.clear_display_buffer()

        # configure firmata for i2c on an UNO
        self.firmata.i2c_config()

        # turn on oscillator
        self.oscillator_set(self.OSCILLATOR_ON)

        # set blink rate
        self.set_blink_rate(self.blink_rate)

        # set brightness
        self.set_brightness(self.brightness)

    def set_blink_rate(self, b):
        """
        Set the user's desired blink rate (0 - 3)
        @param b: blink rate
        """
        if b > 3:
            b = 0  # turn off if not sure
        self.firmata.i2c_write_request(self.board_address,
                                       [(self.HT16K33_BLINK_CMD | self.HT16K33_BLINK_DISPLAYON | (b << 1))])

    def oscillator_set(self, osc_mode):
        """
        Turn oscillator on or off
        @param osc_mode: osc mode (OSCILLATOR_ON or OSCILLATOR_OFF)
        """
        self.firmata.i2c_write_request(self.board_address, [osc_mode])

    def set_brightness(self, brightness):
        """
        Set the brightness level for the entire display
        @param brightness: brightness level (0 -15)
        """
        if brightness > 15:
            brightness = 15
        brightness |= 0xE0
        self.brightness = brightness
        self.firmata.i2c_write_request(0x70, [brightness])

    def set_pixel(self, row, column, color, suppress_write):
        # rows 0,2,4,6,8,10,12,14 are green
        # rows 1,3,5,7,9,11,13,15 are red
        #
        # A row entry consists of 2 bytes, the first always being 0 and the second
        # being the state of the pixel (high or low)
        """

        @param row: pixel row number
        @param column: pix column number
        @param color: pixel color (yellow is both red and green both on)
        @param suppress_write: if true, just sets the internal data structure, else writes out the pixel to the display
        """

        if (row < 0) or (row >= 8):
            print("set_pixel(): ROW out of range")
            return
        if (column < 0) or (column >= 8):
            print("set_pixel(): COLUMN out of range")
            return

        self.display_buffer[row][column] = color

        # output changes to row on display

        green = 0
        red = 0

        # calculate row for green rows and then adjust it for red

        for col in range(0, 8):
            # assemble green data for the row and output
            if self.display_buffer[row][col] == self.LED_GREEN:
                green |= 1 << col
            elif self.display_buffer[row][col] == self.LED_RED:
                red |= 1 << col
            elif self.display_buffer[row][col] == self.LED_YELLOW:
                green |= 1 << col
                red |= 1 << col
            elif self.display_buffer[row][col] == self.LED_OFF:
                green &= ~(1 << col)
                red &= ~(1 << col)

        if not suppress_write:
            self.firmata.i2c_write_request(0x70, [row * 2, green])
            self.firmata.i2c_write_request(0x70, [row * 2 + 1, red])

    def set_bit_map(self, shape, color):
        """
        Populate the bit map with the supplied "shape" and color
        and then write the entire bitmap to the display
        @param shape: pattern to display
        @param color: color for the pattern
        """
        for row in range(0, 8):
            data = shape[row]
            # shift data into buffer
            bit_mask = 0x80
            for column in range(0, 8):
                if data & bit_mask:
                    self.set_pixel(row, column, color, True)
                bit_mask >>= 1
        self.output_entire_buffer()

    def output_entire_buffer(self):
        """
        Write the entire buffer to the display
        """
        green = 0
        red = 0

        for row in range(0, 8):
            for col in range(0, 8):
                if self.display_buffer[row][col] == self.LED_GREEN:
                    green |= 1 << col
                elif self.display_buffer[row][col] == self.LED_RED:
                    red |= 1 << col
                elif self.display_buffer[row][col] == self.LED_YELLOW:
                    green |= 1 << col
                    red |= 1 << col
                elif self.display_buffer[row][col] == self.LED_OFF:
                    green &= ~(1 << col)
                    red &= ~(1 << col)

            self.firmata.i2c_write_request(0x70, [row * 2, green])

            self.firmata.i2c_write_request(0x70, [row * 2 + 1, red])

    def clear_display_buffer(self):
        """
        Set all led's to off.
        """
        for row in range(0, 8):
            self.firmata.i2c_write_request(0x70, [row * 2, 0])
            self.firmata.i2c_write_request(0x70, [((row * 2) + 1), 0])

            for column in range(0, 8):
                self.display_buffer[row][column] = 0

    def close(self):
        """
        close the interface down cleanly

        """
        self.firmata.shutdown()
