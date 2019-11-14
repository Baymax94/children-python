When instantiating pymata3, the `arduino_wait` parameter is set to a default value of 2 seconds. This value specifies the amount of time needed to allow the Arduino to complete a reset cycle. Make sure that this value is set to match the reset needs of your Arduino board type.

Here are some typical reset wait times by board type:

| Board Type    | Seconds       |
|:-------------:|--------------:|
| Uno           | 2 (default)   |
| Leonardo      | 0             |
| Teensy        | 5             |

For other board types, you may need to experiment with this value.

**When retrieving input data, it is preferrable to use a callback method instead of polling for the data value. An example can be found [here](https://gist.github.com/MrYsLab/0b9f125f04f171065af0).**

**When using the pymata3 API and wish to include a sleep in your application, use the pymata3 sleep method instead of time.sleep(). So if your pymata3 instance is called 'board', and you want to sleep for 1 second, you would call board.sleep(1)**

If your code calls a blocking method or function, you may need to convert that code to an asyncio future.
Look at the [source code for the read method](https://mryslab.github.io/pymata-aio/documentation/html/pymata_aio.pymata_serial.PymataSerial-class.html) of pymata_serial to see how to create a non-blocking future from a blocking call.

Examples:
* [Setting digital pin 6 to PWM mode and setting its value to 128](https://github.com/MrYsLab/pymata-aio/blob/master/examples/3_sample.py)

* [Controlling a Servo](https://github.com/MrYsLab/pymata-aio/blob/master/test/servo.py) 

* Control an Adafruit 8x8 bicolor LED display using i2c
    * [A port of the Adafruit-LED-Backpack-Library](https://github.com/MrYsLab/pymata-aio/blob/master/test/i2c/i2c_write/bicolor_display_controller.py)
    * An [application](https://github.com/MrYsLab/pymata-aio/blob/master/test/i2c/i2c_write/i2c_write.py) that uses this library to display a frown face, neutral face, and smiley face on the dispay. 

* [A port of the Sparkun MMA8452Q Accelerometeri2c library.](https://github.com/MrYsLab/pymata-aio/blob/master/examples/mma8452q.py) Requires the use of FirmataPlus.

* [Controlling a Stepper Motor](https://github.com/MrYsLab/pymata-aio/blob/master/test/stepper.py) Requires the use of FirmataPlus.

* [Controlling SR-04 Sonar Distance Device](https://github.com/MrYsLab/pymata-aio/blob/master/test/ping.py) Requires the use of FirmataPlus. 
    * [Wiring Diagram](https://github.com/MrYsLab/pymata-aio/blob/master/documentation/images/ping.png)

* [Creating a tone with a Piezo device](https://github.com/MrYsLab/pymata-aio/blob/master/test/tone_test.py) Requires the use of FirmataPlus.

### Connection Errors:

If you are seeing this message:

`Do you have Arduino connectivity and do you have a Firmata sketch uploaded to the board?`

You may need to use the com_port parameter to explicitly state the com port in use.
