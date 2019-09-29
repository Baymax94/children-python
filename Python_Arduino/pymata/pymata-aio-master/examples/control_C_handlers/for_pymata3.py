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
import signal
import sys


BOARD_LED = 13


# Signal handler to trap control C
def _signal_handler(sig, frame):
    if board is not None:
        print('\nYou pressed Ctrl+C')
        sys.exit(1)


signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)

# add SIGALRM if platform is not windows
if not sys.platform.startswith('win32'):
    signal.signal(signal.SIGALRM, _signal_handler)


def setup():
    board.set_pin_mode(BOARD_LED, Constants.OUTPUT)


def loop():
    print("LED On")
    board.digital_write(BOARD_LED, 1)
    board.sleep(1.0)
    print("LED Off")
    board.digital_write(BOARD_LED, 0)
    board.sleep(1.0)


if __name__ == "__main__":
    board = PyMata3()
    try:
        setup()
        while True:
            loop()
            board.sleep(.1)
    # control-C can cause exceptions - the following suppresses them
    except RuntimeError:
        board.shutdown()
        sys.exit(0)


