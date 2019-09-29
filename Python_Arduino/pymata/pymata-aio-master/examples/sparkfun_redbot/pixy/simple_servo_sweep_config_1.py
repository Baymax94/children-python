#!/usr/bin/env python3
"""
Demo of using the pan and tilt servo kit.

 This demo assumes you have purchased the Pixy pan and tilt kit.  You can connect the servos in two places:
   1. Just plug the servos into servo ports on the Arduino 3, 9, or 10 (NOT 11!).  This demo uses 3 and 10.
   2. Plug the servos in on the Pixy board as recommended here http://cmucam.org/projects/cmucam5/wiki/Assembling_pantilt_Mechanism

 This code assumes you have connected the servos connected to the RedBot board NOT to the Pixy board.

"""

from pymata_aio.pymata3 import PyMata3


WIFLY_IP_ADDRESS = None            # Leave set as None if not using WiFly
WIFLY_IP_ADDRESS = "10.0.1.19"  # If using a WiFly on the RedBot, set the ip address here.
#WIFLY_IP_ADDRESS = "r01.wlan.rose-hulman.edu"  # If your WiFi network allows it, you can use the device hostname instead.
if WIFLY_IP_ADDRESS:
    # arduino_wait is a timer parameter to allow for the arduino to reboot when the connection is made which is NA for WiFly.
    board = PyMata3(arduino_wait=0, sleep_tune=0.0, ip_address=WIFLY_IP_ADDRESS)
else:
    # Use a USB cable to RedBot or an XBee connection instead of WiFly.
    COM_PORT = None # Use None for automatic com port detection, or set if needed i.e. "COM7"
    board = PyMata3(sleep_tune=0.0, com_port=COM_PORT)


# Servo connection locations on the RedBot board.
PIN_PAN_SERVO = 3
PIN_TILT_SERVO = 10


def print_pixy_blocks(blocks):
    """ Prints the Pixy blocks data."""
    print("Detected " + str(len(blocks)) + " Pixy blocks:")
    for block_index in range(len(blocks)):
        block = blocks[block_index]
        print("  block {}: sig: {}  x: {} y: {} width: {} height: {}".format(
                block_index, block["signature"], block["x"], block["y"], block["width"], block["height"]))


def main():
    board.keep_alive(period=2)
    board.pixy_init()
    board.servo_config(PIN_PAN_SERVO)
    board.servo_config(PIN_TILT_SERVO)
    while True:
        for pan_deg in range(90, 170, 2):
            board.analog_write(PIN_PAN_SERVO, pan_deg)
            board.sleep(0.05)
        print_pixy_blocks(board.pixy_get_blocks())
        for pan_deg in range(170, 90, -2):
            board.analog_write(PIN_PAN_SERVO, pan_deg)
            board.sleep(0.05)
        print_pixy_blocks(board.pixy_get_blocks())

        # Test the tilt servo.
        for tilt_deg in range(90, 150, 2):
            board.analog_write(PIN_TILT_SERVO, tilt_deg)
            board.sleep(0.05)
        print_pixy_blocks(board.pixy_get_blocks())
        for tilt_deg in range(150, 30, -2):
            board.analog_write(PIN_TILT_SERVO, tilt_deg)
            board.sleep(0.05)
        print_pixy_blocks(board.pixy_get_blocks())
        for tilt_deg in range(30, 90, 2):
            board.analog_write(PIN_TILT_SERVO, tilt_deg)
            board.sleep(0.05)
        print_pixy_blocks(board.pixy_get_blocks())

        for pan_deg in range(90, 10, -2):
            board.analog_write(PIN_PAN_SERVO, pan_deg)
            board.sleep(0.05)
        print_pixy_blocks(board.pixy_get_blocks())
        for pan_deg in range(10, 90, 2):
            board.analog_write(PIN_PAN_SERVO, pan_deg)
            board.sleep(0.05)
        print_pixy_blocks(board.pixy_get_blocks())

main()
