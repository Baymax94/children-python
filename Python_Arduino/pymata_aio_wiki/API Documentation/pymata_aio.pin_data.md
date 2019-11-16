# [pymata_aio.pin_data](https://htmlpreview.github.io/?https://raw.githubusercontent.com/MrYsLab/pymata-aio/master/documentation/html/pin_data.m.html) 模块
## Classes（类）
`class PinData`  
每个模拟和数字输入引脚均由此类的一个实例描述。 它既包含接收到的最后一个数据值，又包含潜在的回调引用和回调方法类型。 回调方法类型默认为非异步调用，但可以选择将其设置为在需要时使用yield。
### SOURCE
```
class PinData:
    """
    Each analog and digital input pin is described by an instance of
    this class. It contains both the last data value received and a potential
    callback reference and the callback method type.
    The callback method type default is a non-asyncio call,
    but can be optionally be set to use yield from when required.
    """

    def __init__(self):
        # current data value
        self._current_value = 0
        # callback reference
        self._cb = None
        # call back to be executed with "await" or direct call
        # direct call is the default
        self._cb_type = None

    @property
    def current_value(self):
        return self._current_value

    @current_value.setter
    def current_value(self, value):
        self._current_value = value

    @property
    def cb(self):
        return self._cb

    @cb.setter
    def cb(self, value):
        self._cb = value

    @property
    def cb_type(self):
        return self._cb_type

    @cb_type.setter
    def cb_type(self, value):
        self._cb_type = value
```
### Ancestors(in MRO)
+ [PinData](https://htmlpreview.github.io/?https://raw.githubusercontent.com/MrYsLab/pymata-aio/master/documentation/html/pin_data.m.html#pymata_aio.pin_data.PinData)
+ builtins.object
### Static methods
`def __init__(self) `  
Initialize self. See help(type(self)) for accurate signature.
#### SOURCE
```
def __init__(self):
    # current data value
    self._current_value = 0
    # callback reference
    self._cb = None
    # call back to be executed with "await" or direct call
    # direct call is the default
    self._cb_type = None
```
### Instance variables
`var cb`  
`var cb_type`  
`var current_value`

# SOURCE
```
"""
 Copyright (c) 2015-2019 Alan Yorinks All rights reserved.

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


class PinData:
    """
    Each analog and digital input pin is described by an instance of
    this class. It contains both the last data value received and a potential
    callback reference and the callback method type.
    The callback method type default is a non-asyncio call,
    but can be optionally be set to use yield from when required.
    """

    def __init__(self):
        # current data value
        self._current_value = 0
        # callback reference
        self._cb = None
        # call back to be executed with "await" or direct call
        # direct call is the default
        self._cb_type = None

    @property
    def current_value(self):
        return self._current_value

    @current_value.setter
    def current_value(self, value):
        self._current_value = value

    @property
    def cb(self):
        return self._cb

    @cb.setter
    def cb(self, value):
        self._cb = value

    @property
    def cb_type(self):
        return self._cb_type

    @cb_type.setter
    def cb_type(self, value):
        self._cb_type = value
```