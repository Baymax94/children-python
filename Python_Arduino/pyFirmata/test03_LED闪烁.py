#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyfirmata import Arduino, util
import time
# board = Arduino('/dev/tty.usbserial-A6008rIF')
board = Arduino('COM7')

while True:
    board.digital[13].write(0)
    time.sleep(1)
    board.digital[13].write(1)
    time.sleep(1)
