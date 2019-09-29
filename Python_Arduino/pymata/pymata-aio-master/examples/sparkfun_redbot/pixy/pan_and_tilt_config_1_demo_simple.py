#!/usr/bin/env python3
"""
Demo of using the pan servo kit.

 This demo assumes you have purchased the Pixy pan and tilt kit.  You can connect the servos in two places:
   1. Just plug the servos into servo ports on the Arduino 3, 9, or 10 (NOT 11!).  This demo uses 3 and 10.
   2. Plug the servos in on the Pixy board as recommended here http://cmucam.org/projects/cmucam5/wiki/Assembling_pantilt_Mechanism

 This version of the code assumes you have connected the servos connected to the RedBot board NOT to the Pixy board.

 This code doesn't use a fancy solution, just to show that you're not required to make a fancy PD controller.  Keeping it simple.
 Oh also on the keeping it simple front.  This code only does pan.  No tilting is used.

 In addition to the pan and tilt kit you also need all of the setup that was necessary for the pixy_hello_world.py program....
   In order to run this example you of course you need a Pixy and a RedBot with an ICSP header.
   The cable goes such that the red wire of the ribbon cable is on bottom.
   Also make sure you have nothing plugged into pin 11 which is just above that header.
   The Pixy uses pins 11 and 12, but the button does not seem to interfere with Pixy as long as
   it doesn't get pressed (just don't try to use the button and Pixy at the same time).
   You also need to make sure the Pixy has been trained to track a color
     (http://cmucam.org/projects/cmucam5/wiki/Teach_Pixy_an_object).
"""
import math

from pymata_aio.pymata3 import PyMata3


WIFLY_IP_ADDRESS = None            # Leave set as None if not using WiFly
WIFLY_IP_ADDRESS = "10.0.1.19"  # If using a WiFly on the RedBot, set the ip address here.
#WIFLY_IP_ADDRESS = "r01.wlan.rose-hulman.edu"  # If your WiFi network allows it, you can use the device hostname instead.
if WIFLY_IP_ADDRESS:
    # arduino_wait is a timer parameter to allow for the arduino to reboot when the connection is made which is NA for WiFly.
    # Since the Pixy can transmit a lot of data reduce the asyncio sleep time to reduce the possibility of lagging behind messages.
    board = PyMata3(arduino_wait=0, sleep_tune=0.0, ip_address=WIFLY_IP_ADDRESS)
else:
    # Use a USB cable to RedBot or an XBee connection instead of WiFly.
    COM_PORT = None # Use None for automatic com port detection, or set if needed i.e. "COM7"
    board = PyMata3(sleep_tune=0.0, com_port=COM_PORT)

# Pixy x-y position values
PIXY_MIN_X = 0
PIXY_MAX_X = 319
PIXY_MIN_Y = 0
PIXY_MAX_Y = 199
X_CENTER = ((PIXY_MAX_X - PIXY_MIN_X) / 2)
Y_CENTER = ((PIXY_MAX_Y - PIXY_MIN_Y) / 2)

# Servo connection locations on the RedBot board.
PIN_PAN_SERVO = 3

def pixy_value_update(current_pan_angle_deg, prev_pan_move_deg, blocks):
    """ Prints the Pixy blocks data."""
    if len(blocks) > 0:
        pan_error = X_CENTER - blocks[0]["x"]
        if math.fabs(pan_error) < 20.0:
            print("Close enough.")
            return current_pan_angle_deg, 0
        pan_move_deg = 1 if pan_error > 0 else -1
        if prev_pan_move_deg > 0 and pan_move_deg > 0:
            pan_move_deg = 3
        if prev_pan_move_deg < 0 and pan_move_deg < 0:
            pan_move_deg = -3
        current_pan_angle_deg += pan_move_deg
        if current_pan_angle_deg > 150:
            current_pan_angle_deg = 150
        if current_pan_angle_deg < 20:
            current_pan_angle_deg = 20
        print("x: {}  pan_error: {}  pan_move_deg: {}  angle: {}".format(blocks[0]["x"], pan_error, pan_move_deg, current_pan_angle_deg))
        return current_pan_angle_deg, pan_move_deg
    return current_pan_angle_deg, 0


def main():
    pan_servo_angle_deg = 90
    prev_move_deg = 0
    board.keep_alive(period=2)
    board.pixy_init()
    board.servo_config(PIN_PAN_SERVO)
    board.analog_write(PIN_PAN_SERVO, int(pan_servo_angle_deg))
    while True:
        board.sleep(0.05)
        pan_servo_angle_deg, prev_move_deg = pixy_value_update(pan_servo_angle_deg, prev_move_deg, board.pixy_get_blocks())
        board.analog_write(PIN_PAN_SERVO, int(pan_servo_angle_deg))

main()
