"""
 Copyright (c) 2015. 2016, 1017 Alan Yorinks All rights reserved.

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

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants


class TestAnalogInput:
    board = PyMata3(2)
    result = None

    def my_callback(self, data):
        self.result = data
        # print(self.result)

    # set pot to maximum to pass and anything else to fail
    def test_analog_read_write(self):
        # have a potentiometer on A2 and set it to max
        self.board.set_pin_mode(2, Constants.ANALOG)
        self.board.sleep(1)
        av = self.board.analog_read(2)
        assert av == 1023

    # set pot to maximum to pass and anything else to fail
    def test_analog_read_write_cb(self):
        # have a potentiometer on A2 and set it to max
        self.board.set_pin_mode(2, Constants.ANALOG, self.my_callback)
        self.board.sleep(1)
        self.board.analog_read(2)
        assert self.result == [2, 1023,2]

    # set slide switch to on for pass or off for fail
    def test_digital_read_write(self):
        self.board.set_pin_mode(13, Constants.INPUT)
        self.board.set_pin_mode(6, Constants.OUTPUT)
        dv = None
        for i in range(0, 5):
            dv = self.board.digital_read(13)
            self.board.sleep(.1)
        self.board.digital_write(6, dv)
        assert dv == 1
        self.board.sleep(1)
        self.board.digital_write(6, 0)

    # set slide switch to on for pass or off for fail
    def test_digital_read_write_cb(self):
        self.board.set_pin_mode(13, Constants.INPUT, self.my_callback)
        self.board.set_pin_mode(6, Constants.OUTPUT)
        for i in range(0, 5):
            # noinspection PyUnusedLocal
            dv = self.result
            self.board.sleep(.1)
        dv = None
        self.board.digital_write(6, dv)
        assert self.result == [13, 1, 0]
        self.board.sleep(1)
        self.board.digital_write(6, 0)
        self.board.sleep(2)

    def test_get_protocol_version(self):
        pv = self.board.get_protocol_version()
        assert pv == "2.5"

    def test_get_protocol_version_cb(self):
        self.board.get_protocol_version(self.my_callback)
        assert self.result == "2.5"

    def test_get_firmware_version(self):
        fv = self.board.get_firmware_version()
        assert fv == "2.5 FirmataPlus.ino"

    def test_get_firmware_version_cb(self):
        self.board.get_firmware_version(self.my_callback)
        assert self.result == "2.5 FirmataPlus.ino"

    def test_get_capability_report(self):
        cr = self.board.get_capability_report()
        l = len(cr)
        assert l == 192

    def test_get_capability_report_cb(self):
        self.board.get_capability_report(True, self.my_callback)
        l = len(self.result)
        assert l == 192

    def test_get_analog_map(self):
        am = self.board.get_analog_map()
        l = len(am)
        assert l == 20

    def test_get_analog_map_cb(self):
        self.board.get_analog_map(self.my_callback)
        l = len(self.result)
        assert l == 20


    def test_get_pin_state_mode(self):
        self.board.set_pin_mode(5, Constants.OUTPUT)
        ps = self.board.get_pin_state(5)
        assert ps == [5, 1, 0]

    def test_get_pin_state_mode_cb(self):
        self.board.set_pin_mode(5, Constants.INPUT)
        self.board.get_pin_state(5, self.my_callback)
        assert self.result == [5, 0, 0]

    def test_servo(self):
        # observer that motor moves
        # noinspection PyPep8Naming
        SERVO_MOTOR = 5  # servo attached to this pin

        # configure the servo
        self.board.servo_config(SERVO_MOTOR)

        for x in range(0, 2):
            # move the servo to 20 degrees
            self.board.analog_write(SERVO_MOTOR, 20)
            self.board.sleep(1)

            # move the servo to 100 degrees
            self.board.analog_write(SERVO_MOTOR, 100)
            self.board.sleep(1)

            # move the servo to 20 degrees
            self.board.analog_write(SERVO_MOTOR, 20)

            ps = self.board.get_pin_state(5)
            assert ps == [5, 4, 20]

    def test_analog_latch_gt_cb(self):
        self.board.set_pin_mode(2, Constants.ANALOG)
        self.board.set_analog_latch(2, Constants.LATCH_GTE, 512, self.my_callback)
        self.board.sleep(.5)

        assert self.result[Constants.LATCH_CALL_BACK_DATA] >= 512
        assert self.result[Constants.LATCH_CALL_BACK_PIN] == 'A2'

    def test_analog_latch_gt(self):
        self.board.set_pin_mode(2, Constants.ANALOG)
        self.board.set_analog_latch(2, Constants.LATCH_GTE, 512)
        self.board.sleep(.5)
        l = self.board.get_analog_latch_data(2)
        assert l[Constants.LATCHED_DATA] >= 512


