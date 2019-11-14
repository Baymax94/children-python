When using pymata_iot, the message API is a set of JSON messages, that are proxies for pymata_core methods. To view the pymata_core API [click here.](http://htmlpreview.github.io/?https://github.com/MrYsLab/pymata-aio/blob/master/documentation/html/pymata_core.m.html)
The format for these messages is:

`{"method": "METHOD NAME LISTED IN TABLE", "params": PARAMETERS IN TABLE}`

[Click here](https://github.com/MrYsLab/pymata-aio/blob/master/examples/pwm_pin_example.html) to see a sample HTML client.




| Method                    | JSON Parameters From Remote Application | JSON  Paramaters To Remote Application|                           
| ------------------------- |:-------------------  | ------------------------------- |
| analog_read               | [ANALOG_PIN]         |  [PIN, ANALOG_DATA_VALUE] |                                 
| analog_write              | [PIN, WRITE_VALUE] | No Return Message |
| digital_read              | [PIN] | [PIN, DIGITAL_DATA_VALUE]
| digital_write             | [PIN, DIGITAL_DATA_VALUE] | No Return Message |
| disable_analog_reporting  | [PIN] | No Return Message |
| disable_digital_reporting | [PIN] | No Return Message |
| enable_analog_reporting   | [PIN] | [PIN, ANALOG_DATA_VALUE] |
| enable_digital_reporting  | [PIN] | [PIN, DIGITAL_DATA_VALUE] |
| encoder_config            | [PIN_A, PIN_B] | [ENCODER_DATA] |
| encoder_read              | [PIN_A] | [PIN_A, ENCODER_VALUE] |
| get_analog_latch_data     | [ANALOG_PIN] | [ANALOG_PIN, LATCHED_STATE, THRESHOLD_TYPE, THRESHOLD_TARGET, DATA_VALUE, TIME_STAMP ] |
| get_analog_map            | ["null"] | [ANALOG_MAP] |
| get_capability_report     | ["null"] | [RAW_CAPABILITY_REPORT] |
| get_digital_latch_data    | [PIN] | [DIGITAL_PIN, LATCHED_STATE, THRESHOLD_TYPE, THRESHOLD_TARGET, DATA_VALUE, TIME_STAMP ] |
| get_firmware_version      | ["null"] | [FIRMWARE_VERSION] |
| get_pin_state             | [PIN] | [PIN_NUMBER, PIN_MODE, PIN_STATE] |
| get_protocol_version      | ["null"] | [PROTOCOL_VERSION] |
| get_pymata_version        | ["null"] | [PYMATA_VERSION] |
| i2c_config                | [I2C_ADDRESS ] | [i2c_data] |
| i2c_read_data             | [I2C_ADDRESS, I2C_REGISTER, NUMBER_OF_BYTES, I2C_READ_TYPE ] | [DATA] |
| i2c_read_request          | [I2C_ADDRESS, I2C_REGISTER, NUMBER_OF_BYTES, I2C_READ_TYPE ] | [DATA] |
| i2c_write_request         | [I2C_DEVICE_ADDRESS, [DATA_TO_WRITE]] | No Return Message |
| keep_alive                | [KEEP_ALIVE_PERIOD(0 - 10 seconds), MARGIN (.1-.9)] | No Return Message |
| play_tone                 | [PIN, TONE_COMMAND, FREQUENCY(Hz), DURATION(MS)] |  No Return Message | 
| set_analog_latch          | [PIN, THRESHOLD_TYPE, THRESHOLD_VALUE] | [PIN, DATA_VALUE_LATCHED, TIMESTAMP_STRING] |
| set_digital_latch         | [PIN, THRESHOLD (0 or 1)] | [PIN, DATA_VALUE_LATCHED, TIMESTAMP_STRING] |
| set_pin_mode              | [PIN, MODE] | No Return Message |
| set_sampling_interval     | [INTERVAL] |  No Return Message |
| sonar_config              | [TRIGGER_PIN, ECHO_PIN, PING_INTERVAL(default=50), MAX_DISTANCE(default= 200 cm] | [DISTANCE_IN_CM] |
| sonar_read                | [TRIGGER_PIN] | [TRIGGER_PIN, DATA_VALUE] |
| servo_config              | [PIN, MINIMUM_PULSE(ms), MAXIMUM_PULSE(ms)] | No Return Message |
| stepper_config            | [STEPS_PER_REVOLUTION, [PIN1, PIN2, PIN3, PIN4]] | No Return Message |
| stepper_step              | [SPEED, NUMBER_OF_STEPS] | No Return Message |
       
       
**Unsolicited Messages to Client**

| Method                    |  JSON  Paramaters To Remote Application|                           
| ------------------------- |:-------------------|
| analog_message_reply | [PIN, DATA_VALUE] |
| analog_latch_data_reply | [ANALOG_PIN, VALUE_AT_TRIGGER, TIME_STAMP_STRING] |
| digital_message_reply | [PIN, DATA_VALUE] |
| digital_latch_data_reply | [PIN, DATA_VALUE_AT_TRIGGER, TIME_STAMP_STRING] |
| encoder_data_reply | [ENCODER VALUE] |
| i2c_read_request_reply |  [DATA_VALUE] |
| i2c_read_data_reply |  [DATA_VALUE] |
| sonar_data_reply | [DATA_VALUE] |