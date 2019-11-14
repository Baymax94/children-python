Many projects use standalone unit tests for code verification. Because pymata_aio is so heavily hardware dependent, we tested with Arduino boards configured with hardware devices. Code coverage was applied while running the tests to verify that as much code as possible was exercised. The tests used are located in the [_**test**_](https://github.com/MrYsLab/pymata-aio/tree/master/test) directory of the Github distribution.

[PyCharm](https://www.jetbrains.com/pycharm/) was used for all development and testing. Tests were performed using [pytest](http://pytest.org/latest/) when running [test_all.py](https://github.com/MrYsLab/pymata-aio/blob/master/test/test_all.py).

Hardware Used:

[CodeShield Board](http://codeshield.diyode.com/):
* Tested: 
     * analog and digital inputs and outputs including PWM.
     * servos.
     * rotary encoder (FirmataPlus feature).
     * piezo tone generation (FirmataPlus feature).

Standalone Devices:
* Tested:
     * i2c read with the [Sparkfun TMP-102](https://www.sparkfun.com/products/11931)
     * i2c write with the [Adafruit 8x8 Bicolor LED Display](https://www.adafruit.com/products/902)
     * [HC-SR04 Sonar Device](http://www.amazon.com/gp/product/B0089VA3AY?psc=1&redirect=true&ref_=oh_aui_detailpage_o06_s00) (FirmataPlus Feature)
          * Wiring diagram :![sonar](https://raw.github.com/MrYsLab/pymata-aio/master/documentation/images/ping.png).
     * [Stepper Motors](https://www.amazon.com/gp/product/B00JB22IQC?%20psc=1&redirect=trueref_=oh_aui_detailpage_o00_s00)  (FirmataPlus Feature)
    
     
