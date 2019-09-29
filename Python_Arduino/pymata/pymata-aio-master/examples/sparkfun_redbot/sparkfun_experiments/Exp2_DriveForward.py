#!/usr/bin/python
"""
  Exp2_DriveForward -- RedBot Experiment 2

  Drive forward and stop.

  Hardware setup:
  The Power switch must be on, the motors must be connected, and the board must be receiving power
  from the battery. The motor switch must also be switched to RUN.
"""

from pymata_aio.pymata3 import PyMata3
import library.redbot as rb

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

motors = rb.RedBotMotors(board)
# Instantiate the motor control object. This only needs to be done once.


def setup():
    print("Left and right motors at full speed forward")
    motors.drive(255)   # Turn on Left and right motors at full speed forward.
    board.sleep(2.0)    # Waits for 2 seconds
    print("Stop both motors")
    motors.stop()       # Stops both motors
    board.shutdown()


def loop():
    # Nothing here. We'll get to this in the next experiment.
    pass


if __name__ == "__main__":
    setup()

