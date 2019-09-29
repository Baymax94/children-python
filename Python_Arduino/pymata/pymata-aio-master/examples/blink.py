#!/usr/bin/python
"""
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://www.arduino.cc
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

# Arduino LED is on pin 13
BOARD_LED = 13

# If you are having problems connecting, you may
# wish to add some time the arduino_wait parameter.

# replace:
# board = PyMata3()
# with:
# board = PyMata3(arduino_wait=5)

# adjust the arduino_wait value to meet the needs
# of your computer

# instantiate PyMata3
board = PyMata3()


def setup():
    """
    Set the Arduino BOARD_LED pin as an output
    :return:
    """
    board.set_pin_mode(BOARD_LED, Constants.OUTPUT)


def loop():
    """
    Toggle the LED by alternating the values written
    to the LED pin. Wait 1 second between writes.
    Also note the use of board.sleep and not
    time.sleep.
    :return:
    """
    print("LED On")
    board.digital_write(BOARD_LED, 1)
    board.sleep(1.0)
    print("LED Off")
    board.digital_write(BOARD_LED, 0)
    board.sleep(1.0)


if __name__ == "__main__":
    setup()
    while True:
        loop()
