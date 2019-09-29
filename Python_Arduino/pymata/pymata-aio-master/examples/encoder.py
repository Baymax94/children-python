# This is a simple rotary encoder test program.

import sys

from pymata_aio.constants import Constants
from pymata_aio.pymata3 import PyMata3

# encoder pins
ENCODER_A = 14
ENCODER_B = 15


def encoder_callback(data):
    print(data)


# create a PyMata instance
try:
    board = PyMata3()
except KeyboardInterrupt:
    sys.exit(0)

# configure the pins for the encoder

# for callback - enable the next line
# for polling, comment out this line
board.encoder_config(ENCODER_B, ENCODER_A, cb=encoder_callback, cb_type=Constants.CB_TYPE_DIRECT)

# for polling enable this line
# for callback comment out this line
# board.encoder_config(ENCODER_B, ENCODER_A)

print("Change the position on your rotary encoder.")
while 1:
    try:
        board.sleep(.02)
    except KeyboardInterrupt:
        board.shutdown()

    # uncomment for polling
    # print(board.encoder_read(ENCODER_B))
