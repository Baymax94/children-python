#!/usr/bin/python
"""
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://www.arduino.cc
"""

import asyncio

from pymata_aio.pymata_core import PymataCore
from pymata_aio.constants import Constants
import sys
import signal


# Signal handler to trap control C
def _signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C')
    if board is not None:
        loop.run_until_complete(board.shutdown())

signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)

# add SIGALRM if not platform is not windows
if not sys.platform.startswith('win32'):
    signal.signal(signal.SIGALRM, _signal_handler)

# your code goes here
async def blink(my_board):
    """
    Blink LED 13
    @return: No Return Value
    """
    # set the pin mode
    await my_board.set_pin_mode(13, Constants.OUTPUT)

    for i in range(0, 5):
        await my_board.digital_write(13, 1)
        await asyncio.sleep(1)
        await my_board.digital_write(13, 0)
        await asyncio.sleep(1)


if __name__ == "__main__":
    # create a PyMataCore instance and complete the initialization with a call to start_aio()
    board = PymataCore()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(board.start_aio())

    # now execute your code on the loop and shutdown when done
    try:
        loop.run_until_complete(blink(board))
        loop.run_until_complete(board.shutdown())
    except RuntimeError:
        loop.run_until_complete(board.shutdown())
        exit(0)




