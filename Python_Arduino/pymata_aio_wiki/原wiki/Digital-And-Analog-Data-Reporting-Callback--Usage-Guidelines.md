When setting a pin mode in either pymata_core or pymata3, you can optionally specify a callback function that will be called when a data change is reported by the Arduino. Callback functions have an associated callback type that can optionally be set. The callback types are:
```
# callback types
    CB_TYPE_DIRECT = None  # default
    CB_TYPE_ASYNCIO = 1
```
CB_TYPE_DIRECT states that your callback function is a non-asyncio coroutine, and CB_TYPE_ASYNCIO states that your callback function is implemented as an asyncio coroutine.

If you are using pymata3, and are specifying CB_TYPE_DIRECT, and wish to call a pymata3 API method in the callback function, you will need to wrap the function call in an "ensure_future". You will also need to add "import asyncio" to your project. For example, if you wish to call digital_write within the callback, the call would look like this:

```
asyncio.ensure_future(self.board.core.digital_write(13, 0))
```

This "casts" the method call as an asyncio call and calls the pymata_core function directly.

An alternative method is to use CB_TYPE_ASYNCIO and implement your callback as an asyncio coroutine.

The first solution is simpler for those that are not familiar or comfortable with writing asyncio coroutines.


If you don't need to call a pymata-aio method in the callback, for example, updating a variable with the current data value of a pin, then just code as you would any other function.

Data is returned to the callback method in the form an of a 3 element list. The first element is the pin number, the second is data value, and the third is the pin type.

For example, a return value of [2, 1023, 2] indicates that pin 2 returns a value of 1023 and the pin type is analog. The pin type may be found in [constants.py](https://github.com/MrYsLab/pymata-aio/blob/master/pymata_aio/constants.py) in the pin mode section.

**Reenabling The Latch Within The Callback Routine For PyMata3**


This is a sample callback function that performs a latch reenable.
```
def latch_callback(data):
    print(str(data))
    print(time.ctime(int(data[2])))

    # reenable the latch within the callback routine
    asyncio.ensure_future(board.core.board.set_analog_latch(2, Constants.LATCH_GT, 99, latch_callback))

# initial latch enable outside of the callback
board.set_analog_latch(2, Constants.LATCH_GT, 99, latch_callback)
```

Notice the difference in syntax when initially enabling the latch and when it is re-enabled within a callback function

