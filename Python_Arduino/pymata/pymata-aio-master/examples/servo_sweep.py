#!/usr/bin/python
"""
Pymata-aio port of the Arduino Servo --> Sweep Example
"""

from pymata_aio.pymata3 import PyMata3

board = PyMata3()
SERVO_PIN = 5


def setup():
    board.servo_config(SERVO_PIN)


def loop():
    print("Servo up")
    # The range of motion for some servos isn't all the way from 0 degrees to 180 degrees, change as needed.
    for pos in range(0, 180): # Start=0 degrees, Finish=180 degree, (Increment=1 degree which is the default)
        board.analog_write(SERVO_PIN, pos)
        board.sleep(0.015)
    print("Servo down")
    for pos in range(180, 0, -1): # Start=180 degrees, Finish=0 degrees, Increment=-1 degrees (moving down)
        board.analog_write(SERVO_PIN, pos)
        board.sleep(0.015)


if __name__ == "__main__":
    setup()
    while True:
        loop()
