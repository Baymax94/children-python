#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Windows_Arduino
import serial
ser = serial.Serial('COM7', 9600)
print(ser.name)
ser.write(b'hello')
ser.close()
# 其他
with serial.Serial('COM7', 9600, timeout=1) as ser:
    x = ser.read()
    s = ser.read(10)
    line = ser.readline()