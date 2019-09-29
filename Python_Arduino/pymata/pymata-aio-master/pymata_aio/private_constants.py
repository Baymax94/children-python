"""
 Copyright (c) 2015-2019 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""


class PrivateConstants:
    """
    This class contains a set of constants for PyMata internal use .
    """
    # the following defines are from Firmata.h
    # message command bytes (128-255/ 0x80- 0xFF)
    # from this client to firmata
    MSG_CMD_MIN = 0x80  # minimum value for a message from firmata
    REPORT_ANALOG = 0xC0  # enable analog input by pin #
    REPORT_DIGITAL = 0xD0  # enable digital input by port pair
    SET_PIN_MODE = 0xF4  # set a pin to INPUT/OUTPUT/PWM/etc
    SET_DIGITAL_PIN_VALUE = 0xF5  # set a single digital pin value instead of entire port
    START_SYSEX = 0xF0  # start a MIDI Sysex message
    END_SYSEX = 0xF7  # end a MIDI Sysex message
    SYSTEM_RESET = 0xFF  # reset from MIDI

    # messages from firmata
    DIGITAL_MESSAGE = 0x90  # send or receive data for a digital pin
    ANALOG_MESSAGE = 0xE0  # send or receive data for a PWM configured pin
    REPORT_VERSION = 0xF9  # report protocol version

    # start of FirmataPlus defined SYSEX commands
    KEEP_ALIVE = 0x50   # keep alive message
    TONE_DATA = 0x5F  # play a tone at a specified frequency and duration
    ENCODER_CONFIG = 0x60  # create and enable encoder object
    ENCODER_DATA = 0x61  # current encoder position data
    SONAR_CONFIG = 0x62  # configure pins to control a sonar distance device
    SONAR_DATA = 0x63  # distance data returned
    PIXY_CONFIG = 0x64  # configure the Pixy.  Configure has 4 subcommands
    PIXY_DATA = 0x65  # blocks data returned
    # end of FirmataPlus defined SYSEX commands

    SERVO_CONFIG = 0x70  # set servo pin and max and min angles
    STRING_DATA = 0x71  # a string message with 14-bits per char
    STEPPER_DATA = 0x72  # Stepper motor command
    I2C_REQUEST = 0x76  # send an I2C read/write request
    I2C_REPLY = 0x77  # a reply to an I2C read request
    I2C_CONFIG = 0x78  # config I2C settings such as delay times and power pins
    REPORT_FIRMWARE = 0x79  # report name and version of the firmware
    SAMPLING_INTERVAL = 0x7A  # modify the sampling interval

    EXTENDED_ANALOG = 0x6F  # analog write (PWM, Servo, etc) to any pin
    PIN_STATE_QUERY = 0x6D  # ask for a pin's current mode and value
    PIN_STATE_RESPONSE = 0x6E  # reply with pin's current mode and value
    CAPABILITY_QUERY = 0x6B  # ask for supported modes of all pins
    CAPABILITY_RESPONSE = 0x6C  # reply with supported modes and resolution
    ANALOG_MAPPING_QUERY = 0x69  # ask for mapping of analog to pin numbers
    ANALOG_MAPPING_RESPONSE = 0x6A  # reply with analog mapping data

    # reserved values
    SYSEX_NON_REALTIME = 0x7E  # MIDI Reserved for non-realtime messages
    SYSEX_REALTIME = 0x7F  # MIDI Reserved for realtime messages

    # reserved for PyMata
    PYMATA_VERSION = "2.31"

    # each byte represents a digital port
    #  and its value contains the current port settings
    DIGITAL_OUTPUT_PORT_PINS = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    # These values are the index into the data passed by _arduino and
    # used to reassemble integer values
    MSB = 2
    LSB = 1

    # enable reporting for REPORT_ANALOG or REPORT_DIGITAL message
    # sent to firmata
    REPORTING_ENABLE = 1
    # disable reporting for REPORT_ANALOG or REPORT_DIGITAL message
    # sent to firmata
    REPORTING_DISABLE = 0

    # Stepper Motor Sub-commands
    STEPPER_CONFIGURE = 0  # configure a stepper motor for operation
    STEPPER_STEP = 1  # command a motor to move at the provided speed
    STEPPER_LIBRARY_VERSION = 2  # used to get stepper library version number

    # Pixy sub commands
    PIXY_INIT = 0  # Initialize the Pixy object and set the max number of blocks to report
    PIXY_SET_SERVOS = 1  # directly control the pan and tilt servo motors
    PIXY_SET_BRIGHTNESS = 2  # adjust the brightness of the Pixy exposure
    PIXY_SET_LED = 3  # control the color of the Pixy LED

    # Pin used to store Pixy data
    PIN_PIXY_MOSI = 11

