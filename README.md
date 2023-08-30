# TOOMOSS SDK

TOOMOSS USB to CAN, CANFD, LIN, PWM python SDK

[USB2XXX](http://www.toomoss.com/)

## Installation
```
$ python -m venv venv
$ ./venv/Scripts/activate
$ pip install git+https://github.com/mikisama/toomoss_py
```

## Development
```
$ pip install -e .
```

## Example

```py
from toomoss.sdk.usb_device import USB_ScanDevice
from ctypes import c_uint, byref
import sys

DevHandles = (c_uint * 8)()
ret = USB_ScanDevice(byref(DevHandles))
if ret == 0:
    print("No device connected!")
    sys.exit(1)
```
