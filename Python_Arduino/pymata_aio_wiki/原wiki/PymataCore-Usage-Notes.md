When instantiating pymata_core, the `arduino_wait` parameter is set to a default value of 2 seconds. This value specifies the amount of time needed to allow the Arduino to complete a reset cycle. Make sure that this value is set to match the reset needs of your Arduino board type.

Here are some typical reset wait times by board type:

| Board Type    | Seconds       |
|:-------------:|--------------:|
| Uno           | 2 (default)   |
| Leonardo      | 0             |
| Teensy        | 5             |

For other board types, you may need to experiment with this value.

After instantiating the PymataCore class, you must call the start method to complete its instantiation.

[Click here](https://gist.github.com/MrYsLab/df8ec22ea16de6c84d67) to see an example of setting a pin for PWM mode and then setting its output value to 128.

### Connection Errors:

If you are seeing this message:

`Do you have Arduino connectivity and do you have a Firmata sketch uploaded to the board?`

You may need to use the com_port parameter to explicitly state the com port in use.
