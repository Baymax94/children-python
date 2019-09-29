#!/usr/bin/env python3
"""
 Just playing with changing the LED colors on Pixy.
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants


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


def print_pixy_blocks(blocks):
    """ Prints the Pixy blocks data."""
    print("Detected " + str(len(blocks)) + " Pixy blocks:")
    if len(blocks) > 0 and not "signature" in blocks[0]:
        print("Something went wrong.  This does not appear to be a printable block.")
        board.shutdown()
        return
    for block_index in range(len(blocks)):
        block = blocks[block_index]
        print("  block {}: sig: {}  x: {} y: {} width: {} height: {}".format(
                block_index, block["signature"], block["x"], block["y"], block["width"], block["height"]))


def main():
    board.pixy_init()
    board.keep_alive(period=2)
    print("LED color changing")
    while True:
        board.pixy_set_led(255, 0, 0) # Red
        board.sleep(1.0)
        board.pixy_set_led(0, 255, 0) # Green
        board.sleep(1.0)
        board.pixy_set_led(0, 0, 255) # Blue
        board.sleep(1.0)
        board.pixy_set_led(255, 255, 255) # White
        board.sleep(1.0)
        board.pixy_set_led(0, 0, 0) # Off
        board.sleep(0.5)
        for i in range(3):
            board.pixy_set_led(255, 255, 0) # Yellow
            board.sleep(0.1)
            board.pixy_set_led(0, 0, 0) # Off
            board.sleep(0.25)

        print_pixy_blocks(board.pixy_get_blocks())

main()
