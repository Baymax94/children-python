#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyfirmata import Arduino, util
board = Arduino('COM7')
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
a = board.analog[0].read()
print(a)
# board.analog[0].read()
analog_0 = board.get_pin('a:0:i')
b = analog_0.read()
print(b)

pin3 = board.get_pin('d:3:p')
pin3.write(0.6)
