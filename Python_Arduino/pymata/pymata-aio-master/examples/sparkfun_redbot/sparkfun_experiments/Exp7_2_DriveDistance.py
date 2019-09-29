"""
  Exp7_2_DriveDistance -- RedBot Experiment 7.2

  In an earlier experiment, we used a combination of speed and time to
  drive a certain distance. Using the encoders, we can me much more accurate.
  In this example, we will show you how to setup your robot to drive a certain
  distance regardless of the motorPower.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.

  8 Oct 2013 M. Hord
  Revised, 31 Oct 2014 B. Huang
  Revised, 2 Oct 2015 L. Mathews
"""
import math

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
BUTTON_PIN = 12
COUNT_PER_REV = 192    # 4 pairs of N-S x 48:1 gearbox = 192 ticks per wheel rev
WHEEL_DIAM = 2.56 # diam = 65mm / 25.4 mm/in
WHEEL_CIRC = math.pi * WHEEL_DIAM

ENCODER_PIN_LEFT = 16
ENCODER_PIN_RIGHT = 10


def setup():
    board.set_pin_mode(BUTTON_PIN, Constants.INPUT)
    board.digital_write(BUTTON_PIN, 1)  # writing pin high sets the pull-up resistor


def loop():
    # wait for a button press to start driving.
    if board.digital_read(BUTTON_PIN) == 0:
        driveDistance(12, 150)  # drive 12 inches at motor_power = 150
    board.sleep(0.1)


def driveDistance(distance, motor_power):
    left_count= 0
    right_count = 0
    num_rev = distance / WHEEL_CIRC

    # debug
    print("\ndrive_distance() {} inches at {} power for {:.2f} revolutions".format(distance, motor_power, num_rev))

    encoders.clear_enc()  # clear the encoder count
    motors.drive(motor_power)

    while right_count < num_rev * COUNT_PER_REV:
        left_count = encoders.get_ticks(ENCODER_PIN_LEFT)
        right_count = encoders.get_ticks(ENCODER_PIN_RIGHT)
        print("{}       {}       stop once over {:.0f} ticks".format(left_count, right_count, num_rev * COUNT_PER_REV))
        board.sleep(0.1)

    motors.brake()


if __name__ == "__main__":
    setup()
    while True:
        loop()
