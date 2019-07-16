#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Windows_Arduino
import serial
with serial.Serial('COM7', 9600) as ser:
    # ser.baudrate = 9600
    # ser.port = 'COM7'
    # ser.open()
    print(ser.write(b'hello'))