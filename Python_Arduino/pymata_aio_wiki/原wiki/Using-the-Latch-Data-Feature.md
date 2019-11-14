The Latch Data feature is a convenient way to monitor and receive notification for an input data event. It allows you to select the threshold criteria (equal, less than, greater than, etc) for a specific threshold value and receive callback notification when the event occurs. In addition, a time stamp is provided for the time of the occurrence.

For example, you would like to monitor a temperature sensor and would like to be notified when a temperature exceeds some threshold. At the same time, you want to continuously print the current value of a potentiometer every 5 seconds. Here is a code example:

```
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import time

value = {}

# call back function to constantly monitor a potentiometer
def my_callback(data):
    global value
    pin = data[0]
    # data[1] contains the current value for the reporting pin
    value[pin] = (data[1])

# data latch callback routine
# print the full data list and extract the time off occurence
def latch_callback(data):
    print(str(data))
    print(time.ctime(int(data[2])))

    # reenable the latch within the callback routine
    asyncio.ensure_future(board.core.board.set_analog_latch(2, Constants.LATCH_GT, 99, latch_callback))

board = PyMata3()

# enable A2 to monitor a potentiometer and process data changes in the callback
board.set_pin_mode(2, Constants.ANALOG, my_callback)

# enable A5 to monitor a temperature sensor
board.set_pin_mode(5, Constants.ANALOG)

# after enabling analog input, enable data latching.
# the latch will fire if the temperature value exceeds a value of 99
board.set_analog_latch(2, Constants.LATCH_GT, 99, latch_callback)

while True:
    print(value)
    board.sleep(5)
```

Data latches are "one-shots". Once a latch executes, you will need to rearm the latch if you wish to be notified of the event again.

To reenable the latch within the callback when using PyMata3, use the following construct:
```
asyncio.ensure_future(board.core.set_analog_latch)
```
