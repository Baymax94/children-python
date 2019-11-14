Some Examples:

Make sure you have pymata_iot running before running the examples.

* [A Simple HTML Example](https://gist.github.com/MrYsLab/fc6d9def21832f4b743b) (source code).
* [A Full Uno Web Controller](http://mryslab.github.io/pymata-aio/examples/uno_iot_tester.html) (this will bring up a web page). 
Connect your UNO to your computer, start up pymata_iot as described below, click on the link and you will be controlling your UNO from the browser!

JSON messaging is used to communicate between PyMataIOT and your application.

**To see the format for the JSON messages, click on this [link](https://mryslab.github.io/pymata-aio/documentation/html/pymata_aio.pymata_iot.PymataIOT-class.html), then**
**scroll down to the _Method Detail_ section.** 

The parameter field describes the message format for a message coming from your application to pymata_iot. The return field describes the format of messages sent from pymata_aio to your application. 

These messages are totally asynchronous so your application must be ready to receive them at any time. For example, after setting a pin as an input pin (either analog or digital), pymata_aio will start sending data change messages as soon as they start arriving.

[Click here](https://gist.github.com/MrYsLab/fc6d9def21832f4b743b) to see the code for a simple html/JavaScript example of setting a pin for PWM mode and then setting its output value to 128.

## Using PyMataIOT
PymataIOT is invoked from a command line. Here is the usage information from the command line:

```
usage: pymata_iot.py [-h] [-host HOSTNAME] [-port PORT] [-wait WAIT]
                     [-comport COM] [-sleep SLEEP] [-log LOG]
                     [-ardIPAddr AIPADDR] [-ardPort AIPPORT]
                     [-handshake HANDSHAKE]

optional arguments:
  -h, --help            show this help message and exit
  -host HOSTNAME        Server name or IP address
  -port PORT            Server port number
  -wait WAIT            Arduino wait time
  -comport COM          Arduino COM port
  -sleep SLEEP          sleep tune in ms.
  -log LOG              redirect console output to log file
  -ardIPAddr AIPADDR    Arduino IP Address (WiFly
  -ardPort AIPPORT      Arduino IP port (WiFly
  -handshake HANDSHAKE  IP Device Handshake String
```

The default host is "localhost"

The default port is 9000

The default wait is 2 seconds. If you are using a Leonardo, you can set this to zero for quicker boot times.

Here are some typical reset wait times by board type:

| Board Type    | Seconds       |
|:-------------:|--------------:|
| Uno           | 2 (default)   |
| Leonardo      | 0             |
| Teensy        | 5             |

For other board types, you may need to experiment with this value.

If you wish to override the auto com port detection, then set the comport option.

The -sleep option default is 001 seconds. You probably should not change this value.

The -log option default is False, sending all output to the console.

When pymata_iot successfully starts, you should something like the following on your console:

```
pymata_aio Version 1.3	Copyright (c) 2015 Alan Yorinks All rights reserved.

Using COM Port:/dev/ttyUSB0

Initializing Arduino - Please wait... Auto-discovery complete. Found 20 Digital Pins and 6 Analog Pins

```


