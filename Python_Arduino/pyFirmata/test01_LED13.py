#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyfirmata import Arduino, util
# board = Arduino('/dev/tty.usbserial-A6008rIF')
board = Arduino('COM7')
board.digital[13].write(1)

# pyfirmata点亮LED13
