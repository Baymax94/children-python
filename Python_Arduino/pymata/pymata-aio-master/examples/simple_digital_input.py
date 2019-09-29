from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import sys
import signal

# Change the state of a digital input pin and its value will be printed.
# This example uses pin 13, but change to meet your needs


try:
    board = PyMata3()
    board.set_pin_mode(13, Constants.INPUT)
except KeyboardInterrupt:
    sys.exit(0)


# Signal handler to trap control C
def _signal_handler(sig, frame):
    if board is not None:
        print('\nYou pressed Ctrl+C')
        sys.exit(1)


signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)

# add SIGALRM if platform is not windows
if not sys.platform.startswith('win32'):
    signal.signal(signal.SIGALRM, _signal_handler)

while True:
    print(board.digital_read(13))
    board.sleep(.1)
