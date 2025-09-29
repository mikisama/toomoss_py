from ctypes import byref, c_uint

from toomoss_py.api.usb_device import USB_ScanDevice

dev_handles = (c_uint * 8)()
ret = USB_ScanDevice(byref(dev_handles))
if ret == 0:
    raise Exception("ToomossLIN: No device connected!")
