#!/usr/bin/python
"""
  Exp4_MakingSounds -- RedBot Experiment 4

  Push the button (D12) to make some noise and start running!

  Hardware setup:
  Plug the included RedBot Buzzer board into the Servo header labeled 9.

  This sketch was written by SparkFun Electronics, with lots of help from
  the Arduino community. This code is completely free for any use.
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

# Instantiate the motor control object. This only needs to be done once.
motors = rb.RedBotMotors(board)

BUZZER_PIN = 9
BUTTON_PIN = 12


def setup():
    board.set_pin_mode(BUTTON_PIN, Constants.INPUT)  # configures the button as an INPUT
    board.digital_write(BUTTON_PIN, 1)  # Turns ON the pull up on the INPUT
    board.set_pin_mode(BUZZER_PIN, Constants.OUTPUT)  # configures the buzzerPin as an OUTPUT


def loop():
    if board.digital_read(BUTTON_PIN) == 0:
        board.play_tone(BUZZER_PIN, Constants.TONE_TONE, 1000, None)
        board.sleep(0.125) # Wait for 125ms.
        board.play_tone(BUZZER_PIN, Constants.TONE_NO_TONE, 0, 0)  # Stop playing the tone.

        # Turn on Tone again, at 2khz
        board.play_tone(BUZZER_PIN, Constants.TONE_TONE, 2000, 1000)  # Play a 2kHz tone on the buzzer pin
        motors.drive(255) # Drive forward for a while
        board.sleep(1.0)
#         board.play_tone(BUZZER_PIN, Constants.TONE_NO_TONE, 0, 0)  # Not needed since set already.
        motors.brake()
    else:
        pass  # Otherwise do this.

if __name__ == "__main__":
    setup()
    while True:
        loop()
        board.sleep(0.025)





