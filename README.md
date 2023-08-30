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
$ git clone https://github.com/mikisama/toomoss_py
$ cd toomoss_py
$ pip install -e .
```

## Example

```py
import sys
from ctypes import byref, c_uint

from toomoss.sdk.usb_device import USB_ScanDevice

DevHandles = (c_uint * 8)()
ret = USB_ScanDevice(byref(DevHandles))
if ret == 0:
    print("No device connected!")
    sys.exit(1)
```
