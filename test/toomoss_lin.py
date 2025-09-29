from ctypes import byref, c_ubyte, c_uint
from enum import IntEnum

from lin import LinBus

from toomoss_py.api.usb2lin_ex import (
    LIN_EX_CHECK_EXT,
    LIN_EX_CHECK_STD,
    LIN_EX_MASTER,
    LIN_EX_CtrlPowerOut,
    LIN_EX_Init,
    LIN_EX_MasterRead,
    LIN_EX_MasterWrite,
    USB_CloseDevice,
    USB_OpenDevice,
    USB_ScanDevice,
)


class VBAT_Config(IntEnum):
    OUTPUT_0V = 0
    OUTPUT_12V = 1
    OUTPUT_5V = 2


class ToomossLin(LinBus):
    def __init__(
        self,
        index=0,
        channel=0,
        bitrate=19200,
        vbat_output=VBAT_Config.OUTPUT_0V,
        **kwargs,
    ) -> None:
        super().__init__(channel, bitrate, **kwargs)

        self.dev = 0
        self.index = index
        self.init_bitrate = bitrate
        self.vbat_output = vbat_output

        dev_handles = (c_uint * 8)()

        # Scan device
        ret = USB_ScanDevice(byref(dev_handles))
        if ret == 0:
            raise Exception("ToomossLIN: No device connected!")

        self.dev = dev_handles[self.index]

        # Open device
        ret = USB_OpenDevice(self.dev)
        if ret == 0:
            raise Exception("ToomossLIN: Open device faild!")

        self.set_bitrate(bitrate)
        self.is_shutdown = False

    def send(self, id: int, data: bytes):
        data_buffer = (c_ubyte * 8)(*data)
        check_type = LIN_EX_CHECK_STD if id == 0x3C else LIN_EX_CHECK_EXT
        ret = LIN_EX_MasterWrite(
            self.dev,
            self.index,
            id,
            data_buffer,
            len(data),
            check_type,
        )
        if ret < 0:
            raise Exception("ToomossLIN: Could not send message")

    def recv(self, id: int, dlc=8):
        data_buffer = (c_ubyte * 8)()
        ret = LIN_EX_MasterRead(
            self.dev,
            self.index,
            id,
            data_buffer,
        )
        if ret > 0:
            return bytes(data_buffer)

    def set_bitrate(self, bitrate=19200):
        self.bitrate = bitrate
        ret = LIN_EX_Init(self.dev, self.index, bitrate, LIN_EX_MASTER)
        if ret < 0:
            raise Exception("ToomossLIN: Init faild!")

        ret = LIN_EX_CtrlPowerOut(self.dev, self.index, self.vbat_output)
        if ret < 0:
            raise Exception("ToomossLIN: Config VBAT output failed!")

    def shutdown(self):
        if self.is_shutdown:
            return
        self.set_bitrate(self.init_bitrate)
        USB_CloseDevice(self.dev)
        self.is_shutdown = True

    def __del__(self):
        self.shutdown()


def main():
    bus = ToomossLin(index=0, channel=0, bitrate=19200)
    bus.send(0x3C, bytes([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]))
    bus.send(0x3C, bytes([0x7F, 0x02, 0x10, 0x02, 0xFF, 0xFF, 0xFF, 0xFF]))
    bus.shutdown()


if __name__ == "__main__":
    main()
