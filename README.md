# TOOMOSS SDK

TOOMOSS USB to CAN, CANFD, LIN, PWM python SDK

source code adapted from [usb2can_lin_pwm_example](https://gitee.com/toomoss/usb2can_lin_pwm_example)

## Installation
```
$ uv venv
$ uv pip install toomoss_py
```

## Example

```py
from ctypes import byref, c_uint

from toomoss_py.api.usb_device import USB_ScanDevice

dev_handles = (c_uint * 8)()
ret = USB_ScanDevice(byref(dev_handles))
if ret == 0:
    raise Exception("ToomossLIN: No device connected!")
```
