# Startup problems
If your application fails to initialize, here are some things to check:

## Make sure that your USB can support both power and data transfer. 

Some cables only provide power. The easiest way to verify if your cable may be causing the issue or not, is to flash a sketch onto your Arduino board using the IDE with your cable. If the upload succeeds, your cable is working properly.

## Make sure that you have the proper sketch loaded onto the Arduino.

Valid sketches are any of the [FirmataPlus](https://github.com/MrYsLab/pymata-aio/wiki/Uploading-FirmataPlus-to-Arduino) sketches, or [StandardFirmata](https://github.com/MrYsLab/pymata-aio/wiki/Uploading-StandardFirmata-To-Arduino)

**Important Note:** There is a sketch called StandardFirmataPlus included with the Arduino IDE. This is NOT a FirmataPlus sketch and most likely will not work, so please do not install it.

## COM Port Autodetection Selected The Incorrect Port
The autodetection algorithm selects the first COM port that can be opened by the pyserial library. Depending upon how you have your computer configured, the first COM port not be connected to your Arduino. The COM port selected is identified in the startup heading for your pymata-aio application:

```
pymata_aio Version 2.27	Copyright (c) 2015-2018 Alan Yorinks All rights reserved.

Using COM Port:/dev/ttyACM0

Initializing Arduino - Please wait... 
Arduino Firmware ID: 2.5 FirmataPlus32u4.ino
Auto-discovery complete. Found 30 Digital Pins and 12 Analog Pins

```
Here, the COM port */dev/ttyACM0* has been selected. 

To verify that the correct COM port was selected, you can compare the COM port that the Arduino IDE used to flash the Firmata sketch to your board. If they do not match, then you will need to manually specify the COM port in your Python script when instantiating pymata-aio:

```
board = PyMata3(com_port='/dev/ttyACM0')
```

Starting with pymata-aio version 2.27, a utility called "list_serial_ports" is installed automatically when you install pymata-aio.  It requires pyserial version 3.4 or greater to have been installed. Earlier version of pymata-aio installed pyserial version 2.7. To upgrade to the latest version, open a terminal window and type:
```
pip install pyserial --upgrade
```
For Linux and Mac users you may need to type:

```
sudo pip3 install pyserial --upgrade
```

The list_serial_ports utility will list all the serial ports and indicate the manufacturer for any devices connected:
```
$ list_serial_ports
/dev/ttyS0: No Manufacturer Listed
/dev/ttyACM0: Arduino LLC

```
You can also use the list_serial_ports utility to test if your USB cable.

## Run Time Issues

The most common runtime issue is caused by improperly setting up callbacks for notification of signal changes on digital and analog input pins. This [page](https://github.com/MrYsLab/pymata-aio/wiki/Digital-And-Analog-Data-Reporting-Callback--Usage-Guidelines) describes using callbacks.

You can perform a simple runtime test, by running the [blink script](https://github.com/MrYsLab/pymata-aio/blob/master/examples/blink.py). It will flash the LED that is connected to pin 13 of your Arduino. It will also print the changing states of that pin to the console.

## Reporting An Issue

If you have tried all of the above and are still having issues, please file a [new issue](https://github.com/MrYsLab/pymata-aio/issues). Include a copy of your Python script, console output,  and a description of the problem.