#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

BOARD_LED = 13
# board = PyMata3(com_port="/dev/ttyACM0")
board = PyMata3(com_port="COM7")


def setup():
    board.set_pin_mode(BOARD_LED, Constants.OUTPUT)  # 声明引脚为输出
    # board.enable_analog_reporting(0)
    board.set_pin_mode(0, Constants.ANALOG)  # 设置A0, 读模拟信号


def loop():
    try:
        print("LED On")
        board.digital_write(BOARD_LED, 1)  # 写为数字1
        board.sleep(1.0)  # 等待1秒
        print("LED Off")
        board.digital_write(BOARD_LED, 0)  # 写为数字0
        board.sleep(1.0)
        print(board.analog_read(0))  # 读A0，结果为0-1023的一个数

    except:
        board.shutdown()  # 关闭连接, 很有必要


if __name__ == "__main__":
    setup()
    while True:
        loop()
