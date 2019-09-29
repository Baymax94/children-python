#!/usr/bin/python
"""
  Exp3_Turning -- RedBot Experiment 3

  Explore turning with the RedBot by controlling the Right and Left motors
  separately.

  Hardware setup:
  This code requires only the most basic setup: the motors must be
  connected, and the board must be receiving power from the battery pack.
 """

from pymata_aio.pymata3 import PyMata3
import library.redbot as rb
# This line "includes" the RedBot library into your sketch.
# Provides special objects, methods, and functions for the RedBot.


WIFLY_IP_ADDRESS = None            # Leave set as None if not using WiFly
WIFLY_IP_ADDRESS = "10.0.1.19"  # If using a WiFly on the RedBot, set the ip address here.
#WIFLY_IP_ADDRESS = "r01.wlan.rose-hulman.edu"  # If your WiFi network allows it, you can use the device hostname instead.
if WIFLY_IP_ADDRESS:
    # arduino_wait is a timer parameter to allow for the arduino to reboot when the connection is made which is NA for WiFly.
    board = PyMata3(arduino_wait=0, ip_address=WIFLY_IP_ADDRESS)
else:
    # Use a USB cable to RedBot or an XBee connection instead of WiFly.
    COM_PORT = None # Use None for automatic com port detection, or set if needed i.e. "COM7"
    board = PyMata3(com_port=COM_PORT)

board.keep_alive(2) # Important because it will stop the motors if you stop the Python program.
motors = rb.RedBotMotors(board)
# Instantiate the motor control object. This only needs to be done once.


def setup():
    print("Driving forward")
    # drive forward -- instead of using motors.drive(); Here is another way.
    motors.right_motor(150)  # Turn on right motor clockwise medium power (motorPower = 150)
    motors.left_motor(150)  # Turn on left motor counter clockwise medium power (motorPower = 150)
    board.sleep(1.0)  # Waits for 1000 ms.
    motors.brake();

    print("Pivot-- turn to right")
    # pivot -- spinning both motors CCW causes the RedBot to turn to the right
    motors.right_motor(-100)  # Turn on right motor clockwise medium power (motorPower = 150)
    motors.left_motor(-100)  # Turn on left motor counter clockwise medium power (motorPower = 150)
    board.sleep(0.500)
    motors.brake()
    board.sleep(0.500)

    print("Driving Straight to Finish")
    # drive forward -- instead of using motors.drive(); Here is another way.
    motors.right_motor(150)  # Turn on right motor clockwise medium power (motorPower = 150)
    motors.left_motor(-150)  # Turn on left motor counter clockwise medium power (motorPower = 150)
    motors.drive(255)
    board.sleep(1.0)
    motors.brake()  # brake() motors


def loop():
    # Figure 8 pattern -- Turn Right, Turn Left, Repeat
    print("Veering Right")
    motors.left_motor(-200)  # Left motor CCW at 200
    motors.right_motor(80)   # Right motor CW at 80
    board.sleep(2.0)
    print("Veering Left")
    motors.left_motor(-80)   # Left motor CCW at 80
    motors.right_motor(200)  # Right motor CW at 200
    board.sleep(2.0)
    pass


if __name__ == "__main__":
    setup()
    while True:
        loop()
