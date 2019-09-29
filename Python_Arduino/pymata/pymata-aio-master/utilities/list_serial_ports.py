"""
 Copyright (c) 2018 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import serial.tools.list_ports
import sys


# This utility will find all of the serial ports on your computer
# and will list the port device and its manufacturer for usb serial
# devices like Arduino.

# example
def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        try:
            if port.manufacturer:
                print(port.device + ': ' + port.manufacturer)
            else:
                print(port.device + ': No Manufacturer Listed')
        except AttributeError:
            print("\nThis utility requires that pyserial version 3.4 or greater is installed.")
            sys.exit(0)


def lsp():
    list_serial_ports()


if __name__ == '__main__':
    lsp()
