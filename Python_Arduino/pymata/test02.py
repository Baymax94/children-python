#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

Trig = 7
Echo = 8
# board = PyMata3(com_port="/dev/ttyACM0")
board = PyMata3(com_port="COM6")

'''
def checkdistance():
    board.digital_write(Trig,0)
    board.sleep(0.002)
    board.digital_write(Trig,1)
    board.sleep(0.01)
    board.digital_write(Trig,0)
    distance=board.int_read(0)/58.00
    board.sleep(0.01)
    return distance
'''


def setup():
    board.set_pin_mode(Trig, Constants.OUTPUT)  # 声明引脚为输出
    # board.set_pin_mode(Echo, Constants.INPUT)  # 声明引脚为输入
    board.set_pin_mode(Echo, Constants.ANALOG)


def loop():
    try:
        board.digital_write(Trig, 0)
        board.sleep(0.002)
        board.digital_write(Trig, 1)
        board.sleep(0.01)
        board.digital_write(Trig, 0)
        # distance = board.int_read(Echo)/58.00     # 对应arduino的pulseIn()，缺失
        distance = board.analog_read(Echo)/58.00
        board.sleep(0.01)
        print(distance)

    except:
        board.shutdown()


if __name__ == "__main__":
    setup()
    while True:
        loop()

# 超声波
