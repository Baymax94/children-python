"""
Exp9_SerialDrive -- RedBot Experiment 9

  The first step to controlling the RedBot remotely is to first drive it
  from the Serial Monitor in a tethered setup.

  Hardware setup:
  After uploading this sketch, keep the RedBot tethered to your computer with
  the USB cable. Open up the Serial Monitor to send commands to the RedBot to
  drive.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.

  15 Dec 2014 B. Huang

  This experiment was inspired by Paul Kassebaum at Mathworks, who made
  one of the very first non-SparkFun demo projects and brought it to the
  2013 Open Hardware Summit in Boston. Thanks Paul!

  Revised, 2 Oct, 2015 L. Mathews
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


def setup():
    print("Type in a number between -255 to 255 to drive at that speed.")

def loop():
    speed = int(input()) # Note, adding a board.keep_alive to this program would be bad due the block nature of the input() command.
    speed = throttle(speed)
    motors.drive(speed)


def throttle(n, min_value=-255, max_value=255):
    """Constraining the speed value between -255:255"""
    return max(min(max_value, n), min_value)

if __name__ == "__main__":
    setup()
    while True:
        loop()


