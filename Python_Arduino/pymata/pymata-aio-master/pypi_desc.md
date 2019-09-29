

pymata_aio is a high performance, non-blocking, Python asyncio client
for the Firmata Protocolthat supports the complete StandardFirmata
protocol.

Major features
==============

* Python 3.5+ compatible.

* Choose From 3 Included APIs
     * pymata_core - a pure asyncio method call API.
     * pymata3 - A non-asyncio proxy for pymata_core
     * pymata_iot - A websocket based backed to control an Arduino over a Web page.

* Implements 100% of the StandardFirmata Protocol (StandardFirmata 2.5.3).

* Auto-detects Arduino COM ports.

* FirmataPlus (enhanced StandardFirmata sketch) included with distribution. It adds support for:
     * HC-SR04 Ultrasonic Distance Sensors using a single pin.
     * Stepper Motors.
     * Piezo Tone Generation.
     * 2 Pin Rotary Encoder Support.

* FirmataPlusRB (enhanced StandaradFirmata sketch to control a SparkFun Redbot. It adds support for:
     * Piezo Tone Generation.
     * Wheel encoders.
     * RedBot Accelerometer.

* Ability to automatically capture and time-stamp user specified analog and digital transient input events on a per-pin basis.
* All 3 APIs support callback as well as a polled interface.


