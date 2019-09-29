#!/usr/bin/env python3
"""
Basic demo of reporting Pixy data.

 This sketch is a good place to start if you're just getting started with
 Pixy and pymata-aio.  This program simply prints the detected object blocks
 much like the standard Pixy Hello World demo for Arduino.

 In order to run this example you of course you need a Pixy and a RedBot with an ICSP header.
 The cable goes such that the red wire of the ribbon cable is on bottom.
 Also make sure you have nothing plugged into pin 11 which is just above that header.
 The Pixy uses pins 11 and 12, but the button does not seem to interfere with Pixy as long as
 it doesn't get pressed (just don't try to use the button and Pixy at the same time).

 You also need to make sure the Pixy has been trained to track a color
  (http://cmucam.org/projects/cmucam5/wiki/Teach_Pixy_an_object).
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

# Much like digital and analog readings, you can read Pixy data by either registering callback function that
# is called when a new value is received or you can read the most recent value received at any time.
use_pixy_callback = True    # Use the callback function to be called every time Pixy data arrives.
#use_pixy_callback = False  # Use board.pixy_get_blocks() to get the value on demand

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
    if use_pixy_callback:
        # Use a callback to display the Pixy readings.  (very simple callback)
        board.pixy_init(cb=print_pixy_blocks, cb_type=Constants.CB_TYPE_DIRECT)
    else:
        # Use the pixy_block property to display the readings.
        board.pixy_init()

    board.keep_alive(period=2)
    # Flash the LED while killing time.
    board.set_pin_mode(13, Constants.OUTPUT)
    while True:
        board.digital_write(13, 1)
        board.sleep(0.25)
        board.digital_write(13, 0)
        board.sleep(0.25)
        if not use_pixy_callback:
            print_pixy_blocks(board.pixy_get_blocks())

main()
