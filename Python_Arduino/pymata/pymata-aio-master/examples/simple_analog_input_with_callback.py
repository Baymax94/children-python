from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import sys
import signal


# this program monitors the A2 pin. Modify to meet your needs

def my_callback(data):
    # data[0] is the pin number and data[1] is the changed value
    print(data[1])


try:
    board = PyMata3()
    board.set_pin_mode(2, Constants.ANALOG, my_callback)
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
    board.sleep(.1)
