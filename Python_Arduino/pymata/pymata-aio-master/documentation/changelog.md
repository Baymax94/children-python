# Change Log

## Release 2.30
18 May 2019
* Added parameter to generate exceptions instead of exiting

## Release 2.29
12 May 2019
* Accepted Pull Request #93

## Release 2.28
09 November 2018

* Fixed issue #87
* Updated copyright strings for FirmataPlus files - no code changes

## Release 2.27
22 October 2018

* Fixed warnings in FirmataPlus scripts for Default warning level in Arduino IDE.
* Fixed issue #85 Using current Arduino IDE, FirmataPlus.ino gives warnings when compiled.
* Fixed issue #86 Rotary Encoder support not functioning.
* Added some example code for the rotary encoder, simple digital and anlog  input.
* Added a command utility to list the serial ports to help debug. This is automatically
  installed with pymata-aio. Just type list_serial_ports in a console to see the serial ports.

## Release 2.26
20 October 2018

* Incorporates changes for issues #82, 83, and 84
* Default arduino_wait time increased from 2 to 4 seconds
* Timeout in get_firmware_version increased to 4 seconds


## Release 2.25
23 August 2018

* Incorporates pull request # 74

## Release 2.24
12 August 2018

* Minor code cleanup

## Release 2.23

5 July 2018

* Removed restriction of pyserial version 2.7 - newest version can now be used

## Release 2.22
4 July 2018

* Aligned pin types with StandardFirmata to support pullup input

## Release 2.21
15 June 2018

* Extended timeout for analog map to report back - now 4 seconds.

## Release 2.20
16 April 2018

* Modified comments to generate pdoc API documentation.
* No functional changes.


8 April 2018

* Typo fixes and updates to support the new pypi.org page

## Release 2.19
28 September 2017

* Fixes bug in accepting analog data from a Mega 2560 pin 15.

## Release 2.18 (overwrites 2.17)

17 September 2017

* Licensing changed from GPL V3 to GPL Affero V3
* Callbacks now report pin type. See [this wiki page](https://github.com/MrYsLab/pymata-aio/wiki/Digital-And-Analog-Data-Reporting-Callback--Usage-Guidelines) for details. Note this should not be a breaking change. All existing applications should be able to run without modification.
* Bumped up version number that was incorrect in 2.17

## Release 2.16

24 August 2016

* This is a minor bug fix release

  * Added a 2 second timeout for retrieiving Firmata Firmware Verison
  * If the request times out, the application will exit since there is no connectivity to the Arduino.

## Release 2.15

31 July 2016

* Added support for the SET_DIGITAL_PIN_VALUE Firmata command

  * This release is now fully compatible with StandardFirmata 2.5.3
  * On-Line API Documents Updated to reflect new command

* Update pymata_iot.py to use websockets instead of autobahn.

  * setup.py added dependency of websockets and removed autobahn/txaio dependencies

## Release 2.14

26 July 2016


* Arduino Firmware Version information is printed as part of start-up banner
* All FirmataPlus versions were re-baselined against StandardFirmata 2.5.3
* An additional FirmataPlus variant was created to support AVR 32u4 boards.
* Corrected 2 calls to asyncio.sleep in pymata_serial.py that were missing awaits. These fixes should not affect the performance of the pymata_aio library, and therefore updating to this release from 2.13 is optional.
* Forced txaio (required by autobahn) to an earlier release (2.1.0) to avoid warnings generated in latest version.

## Release 2.13

21 April 2016

* Added additional Arduino board type detection
* Updated setup.py to bring in specific versions of pyserial and autobahn.
* Version 2.12 not accepted on PyPi

## Release 2.12

21 April 2016

* Added additional Arduino board type detection
* Updated setup.py to bring in specific versions of pyserial and autobahn.

## Release 2.11

18 February 2016

* Assures all data sent to Firmata consists of 7 bit bytes

## Release 2.10

11 February 2016

* Additional Fixes [issue #35](https://github.com/MrYsLab/pymata-aio/issues/35) and [issue #36](https://github.com/MrYsLab/pymata-aio/issues/36)

## Release 2.9

9 February 2016

* Fixes [issue #35](https://github.com/MrYsLab/pymata-aio/issues/35) and [issue #36](https://github.com/MrYsLab/pymata-aio/issues/36)

## Release 2.8

3 December 2015

* Fixes [issue #32](https://github.com/MrYsLab/pymata-aio/issues/32).
* Code cleanup for consistency.


##Release 2.7

9 November 2015

### New Feature Added
* [Pixy Cam](http://charmedlabs.com/default/pixy-cmucam5/) support courtesy of Dave Fisher and Leigh Andrew Mathews of the [Rose Hulman Institute of Technology](http://www.rose-hulman.edu/)
   * pymata_core and pymata3 updated for Pixy Cam support
   * A new firmata sketch, FirmataPlusRBPixy has been added to the Arduino libraries

### Updates
* All FirmataPlus sketches have been updated for the latest dependencies libraries
* The sleep_tune paramater default was modified to 0.0001 for pymata_core and added to pymata3

### Bug Fixes
* Typos corrected for stepper_config and a missing await in set_sampling_interval

##Release 2.6

14 October 2015

### New Feature Added
* Added new KeepAlive feature
    * Requires Use of FirmataPlus, FimrataPlusRB or FirmataPlusLBT
    * Enable with a call to keep_alive, passing in a keep alive period.
        * Keep alives may be set between 1 and 10 seconds.
        * Setting the period to 0 seconds disables the keep alive timer.

##Release 2.5

11 October 2015

* Merged latest changes for SparkFun RedBot experiments
* Fixed bug in accepting com_port parameter
* pymata_iot sends reset to Arduino upon exit

##Release 2.4

4 October 2015

* Control C handling removed from pymata_aio internals.
    * Control C handling must be done by appliction
    * Control C handler examples my be viewed [here](https://github.com/MrYsLab/pymata-aio/tree/master/examples/control_C_handlers)

##Release 2.3

3 October 2015

* Repaired bug in control C handling


##Release 2.2

3 October 2015

* Added IP support for WiFly module allowing wireless SparkFun RedBot operations
* FirmataPlus and FirmataPlusRB resets Arduino code and variables module when send_reset is called
* Cleanup of Control-C handling


##Release 2.1

## This is a major release migration from Python 3.4.3 to Python 3.5

28 Aug 2015

* Converted all code to be Python 3.5 compliant.
    * Removed all @asyncio.coroutine decorators and replaced with "async"
    * Replaced all "yield from" to "await"
* Modified FirmataPlusRB.ino systemResetCallback() to set encoder present to false
* API documentation is now Sphinx generated


##Release 1.9
28 Aug 2015

Sparkfun Redbot Support Changes

* Changed encoder pulse detection in FirmataPlusRB from both leading and rising edges to rising edge only.

* Added paramater in pymata3, encoder_config to support hall effect sensors and be in sync with pymata_core.


##Release 1.8
21 Aug 2015

* Bug fix release for pymata3 - changed all calls from pymata3 to pymata_core to loop.run_until_complete
* Duration parameter in play_tone for pymata3 set to a default of None

##Release 1.7
20 Aug 2015

Fixed issue #20 - Tone not properly activated when using pymata3

FirmataPlusRB updated to report encoder readings every 100 ms.

##Release 1.6
19 Aug 2015

* Modifications in anticipation of the upcoming release of our [Sparkfun RedBot]
(https://www.sparkfun.com/products/12649) support library.

    * Modified data format returned for hall effect wheel encoders.

    * Added an additional Arduino sketch, FirmataPlusRB, that will support the redbot sensors and actuators.

##Release 1.5
15 Aug 2015

* Callbacks for both pymata_core and pymata3 can selected to be either asyncio coroutines or direct calls.
    * Default is direct call.

* Option provided in encoder_config() for support of hall effect wheel encoders.

* Minor bug fixes.

* Code cleanup.

##Release 1.4
1 Aug 2015

* Auto Detection for OS X ports repaired from release 1.3. Tested and functioning now.


##Release 1.3
23 July 2015

* Auto detection of OS X serial ports added

* Added a logging feature to optionally redirect console output to a log file.

* Removed SIGALRM from Control-C handler to support Windows.


##Release 1.2

19 July 2015

Data format returned from i2c_read_request was normalized from Firmata 2byte format to expected data
representation.



##Release 1.1

18 July 2015

* Fixed bug in data returned from i2c multi-byte read

* Added ability to optionally set "repeated start" for i2c read command
    * Requires the use of FirmataPlus sketch.
    * StandardFirmata Future Release will support this feature, but not currently.

* FirmataPlus updated to be in sync with StandardFirmata 2.4.3

* Updated private_constants.py and constants.py to be consistent with StandardFirmata 2.4.3


