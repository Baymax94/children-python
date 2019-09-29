"""//***********************************************************************
 * Exp6_LineFollowing_IRSensors -- RedBot Experiment 6
 *
 * This code reads the three line following sensors on A3, A6, and A7
 * and prints them out to the Serial Monitor. Upload this example to your
 * RedBot and open up the Serial Monitor by clicking the magnifying glass
 * in the upper-right hand corner.
 *
 * This sketch was written by SparkFun Electronics,with lots of help from
 * the Arduino community. This code is completely free for any use.
 *
 * 8 Oct 2013 M. Hord
 * Revised, 31 Oct 2014 B. Huang
 * Revices, 2 Oct 2015 L Mathews
 ***********************************************************************/"""

import sys
import signal

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

board.keep_alive(2) # Important because it will stop the analog sensor stream if you stop the Python program.

LEFT_LINE_FOLLOWER = 3  # pin number assignments for each IR sensor
CENTRE_LINE_FOLLOWER = 6
RIGHT_LINE_FOLLOWER = 7

IR_sensor_1 = rb.RedBotSensor(board, LEFT_LINE_FOLLOWER)
IR_sensor_2 = rb.RedBotSensor(board, CENTRE_LINE_FOLLOWER)
IR_sensor_3 = rb.RedBotSensor(board, RIGHT_LINE_FOLLOWER)


def signal_handler(sig, frame):
    """Helper method to shutdown the RedBot if Ctrl-c is pressed"""
    print('\nYou pressed Ctrl+C')
    if board is not None:
        board.send_reset()
        board.shutdown()
    sys.exit(0)


def setup():
    signal.signal(signal.SIGINT, signal_handler)
    print("Welcome to Experiment 6!")
    print("------------------------")


def loop():
    board.sleep(0.1)
    print("IR Sensor Readings: {},   {},    {}".format(IR_sensor_1.read(), IR_sensor_2.read(), IR_sensor_3.read()))


if __name__ == "__main__":
    setup()
    while True:
        loop()
