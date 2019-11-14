
**_FirmataPlus_** is an enhanced version of StandardFirmata that is included with this distribution.

PLEASE NOTE: **FirmataPlus** is different than StandardFirmataPlus. StandardFirmataPlus **WILL NOT WORK CORRECTLY**.

FirmataPlus provides support for:

1. HC-SR04 Sonar distance devices
1. Rotary Encoder (not supported for FirmataPlus32u4)
1. Stepper Motor Support
1. Piezo tone generation.

Leonardo and Mega 2560 users, please upload **_FirmataPlus32u4_** instead of FirmataPlus



**FirmataPlus** is distributed as a zip file. If you downloaded the pyamta_aio distribution from Github and extracted the files, you will find a libraries.zip file in the FirmataPlus directory. You can also directly download it [here](https://github.com/MrYsLab/pymata-aio/blob/master/FirmataPlus/libraries.zip). Click on the "view raw" button to download.

Open the Arduino IDE and select File/Preferences to determine your _sketchbook_ location. 

![](https://github.com/MrYsLab/pymata-aio/blob/master/documentation/images/arduinoSketchDir.png)

Close the Arduino IDE and extract the libraries.zip file into the sketchbook location directory.

Re-open the Arduino IDE, select File/Examples/FirmataPlus/FiramataPlus and upload to your Arduino.

![standardfirmata](https://github.com/MrYsLab/pymata-aio/blob/master/documentation/images/firmataplus.png)

If you are seeing warnings when you compile the FirmataPlus sketches in the Arduino IDE, 
make sure you have set the compiler warnings level to "Default" in the File/Preferences screen. If you are still seeing warnings, get the latest copy of libraries.zip and reinstall.