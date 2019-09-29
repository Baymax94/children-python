#!/usr/bin/env python3
"""
Drives the RedBot motors around without using a library at all.
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

# RedBot motor pins from RedBot.h
L_CTRL_1 = 2
L_CTRL_2 = 4
PWM_L = 5

R_CTRL_1 = 7
R_CTRL_2 = 8
PWM_R = 6

board = PyMata3()


def setup():
    """Setup pins"""
    print("Simple drive")
    board.set_pin_mode(L_CTRL_1, Constants.OUTPUT)
    board.set_pin_mode(L_CTRL_2, Constants.OUTPUT)
    board.set_pin_mode(PWM_L, Constants.PWM)
    board.set_pin_mode(R_CTRL_1, Constants.OUTPUT)
    board.set_pin_mode(R_CTRL_2, Constants.OUTPUT)
    board.set_pin_mode(PWM_R, Constants.PWM)


def loop():
    """Function that gets called again as soon as it finishes (forever)."""
    print("Straight")
    board.digital_write(L_CTRL_1, 1)
    board.digital_write(L_CTRL_2, 0)
    board.analog_write(PWM_L, 245)
    board.digital_write(R_CTRL_1, 1)
    board.digital_write(R_CTRL_2, 0)
    board.analog_write(PWM_R, 245)
    board.sleep(2.0)

    print("CW spin")
    board.digital_write(L_CTRL_1, 1)
    board.digital_write(L_CTRL_2, 0)
    board.analog_write(PWM_L, 245)
    board.digital_write(R_CTRL_1, 0)
    board.digital_write(R_CTRL_2, 1)
    board.analog_write(PWM_R, 245)
    board.sleep(2.0)

    print("CCW spin")
    board.digital_write(L_CTRL_1, 0)
    board.digital_write(L_CTRL_2, 1)
    board.analog_write(PWM_L, 245)
    board.digital_write(R_CTRL_1, 1)
    board.digital_write(R_CTRL_2, 0)
    board.analog_write(PWM_R, 245)
    board.sleep(2.0)

    print("Stop")
    board.digital_write(L_CTRL_1, 1)
    board.digital_write(L_CTRL_2, 0)
    board.analog_write(PWM_L, 0)
    board.digital_write(R_CTRL_1, 1)
    board.digital_write(R_CTRL_2, 0)
    board.analog_write(PWM_R, 0)
    board.sleep(5.0)

if __name__ == "__main__":
    setup()
    while True:
        loop()
