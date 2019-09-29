"""
  Exp7_1_RotaryEncoder -- RedBot Experiment 7

  Knowing where your robot is can be very important. The RedBot supports
  the use of an encoder to track the number of revolutions each wheel has
  made, so you can tell not only how far each wheel has traveled but how
  fast the wheels are turning.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.

  8 Oct 2013 M. Hord
  Revised, 31 Oct 2014 B. Huang+
  Revised, 2 Oct 2015 L. Mathews
 """

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
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

board.keep_alive(2) # Important because it will stop the encoder data stream if you stop the Python program.

motors = rb.RedBotMotors(board)
encoders = rb.RedBotEncoder(board)

ENCODER_PIN_LEFT = 16
ENCODER_PIN_RIGHT = 10

BUTTON_PIN = 12

COUNTS_PER_REV = 192    # 4 pairs of N-S x 48:1 gearbox = 192 ticks per wheel rev


def setup():
    board.set_pin_mode(BUTTON_PIN, Constants.INPUT)
    board.digital_write(BUTTON_PIN, 1)  # writing pin high sets the pull-up resistor
    print("Left     Right")
    print("==============")


def loop():
    # wait for a button press to start driving.
    if board.digital_read(BUTTON_PIN) == 0:
        encoders.clear_enc()  # Reset the counters
        motors.drive(150)  # Start driving forward

    left_count = encoders.get_ticks(ENCODER_PIN_LEFT)
    right_count = encoders.get_ticks(ENCODER_PIN_RIGHT)

    print("{}       {}".format(left_count, right_count))  # stores the encoder count to a variable

    #  if either left or right motor are more than 5 revolutions, stop
    if left_count >= 5 * COUNTS_PER_REV or right_count >= 5 * COUNTS_PER_REV:
        motors.brake()


if __name__ == "__main__":
    setup()
    while True:
        loop()
        board.sleep(0.025) # Add a delay to allow other processes to finish (like printing)
