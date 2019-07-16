#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Windows_Arduino
import serial
ser = serial.Serial()
# ser.baudrate = 19200
ser.baudrate = 9600
ser.port = 'COM7'
print(ser)
ser.open()
print(ser.is_open)
ser.close()
print(ser.is_open)