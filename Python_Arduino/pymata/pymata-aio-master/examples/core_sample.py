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
"""

import asyncio

from pymata_aio.pymata_core import PymataCore
from pymata_aio.constants import Constants


async def pin_6_pwm_128(my_board):
    """
    Set digital pin 6 as a PWM output and set its output value to 128
    @param my_board: A PymataCore instance
    @return: No Return Value
    """
    # set the pin mode
    await my_board.set_pin_mode(6, Constants.PWM)

    # set the pin to 128
    await my_board.analog_write(6, 128)

    # let the led stay lit for 3 seconds
    await asyncio.sleep(3)

    # shutdown
    await my_board.shutdown()


# create a PyMataCore instance and complete the initialization with a call to start()
board = PymataCore()
board.start()

# get the loop, and execute pin6_pwm_128
loop = asyncio.get_event_loop()
loop.run_until_complete(pin_6_pwm_128(board))
