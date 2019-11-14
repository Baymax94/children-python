The preferred way to use the tone feature is to enable a continuous tone, then set a sleep for the desired tone duration, and then to turn the tone off.

Here is an example:
```
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

BEEPER = 3  # pin that piezo device is attached to

# create a PyMata instance
board = PyMata3()

# play a continuous tone, wait 5 seconds and then turn tone off
board.play_tone(BEEPER, Constants.TONE_TONE, 1000)
board.sleep(5)
board.play_tone(BEEPER, Constants.TONE_NO_TONE, 1000)

board.shutdown()

```